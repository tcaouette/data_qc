import json

class JSONReporter(AbstractReporter):
    async def generate(self, report: QualityReportConfig) -> str:
        return report.json(indent=2)