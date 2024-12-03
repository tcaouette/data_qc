# engine.py
from typing import Dict, Any, List
from .adapters.factory import AdapterFactory
from .profilers.factory import ProfilerFactory
from .quality_checks.factory import QualityCheckFactory
from .reporters.factory import ReporterFactory
from .core.config import QualityReportConfig

class QualityEngine:
    def __init__(self):
        self.adapter_factory = AdapterFactory()
        self.profiler_factory = ProfilerFactory()
        self.check_factory = QualityCheckFactory()
        self.reporter_factory = ReporterFactory()

    async def run_analysis(self, config: Dict[str, Any]) -> str:
        adapter = self.adapter_factory.create_adapter(
            config["adapter_type"],
            config["adapter_config"]
        )
        await adapter.connect()
        
        data = await adapter.read_data()
        source = await adapter.get_metadata()
        
        profiler = self.profiler_factory.create_profiler(config["profiler_type"])
        profile = await profiler.profile(data, source)
        
        checks = []
        for check_config in config["checks"]:
            check = self.check_factory.create_check(
                check_config["type"],
                check_config["params"]
            )
            result = await check.check(data, source)
            checks.append(result)
        
        report = QualityReportConfig(
            source=source,
            checks=checks,
            profile=profile
        )
        
        reporter = self.reporter_factory.create_reporter(config["reporter_type"])
        return await reporter.generate(report)