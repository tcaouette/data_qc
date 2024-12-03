from ..abstract_check import AbstractQualityCheck
from ...core.config import QualityCheckConfig, QualityCheckSeverity

class CompletenessCheck(AbstractQualityCheck):
    def __init__(self, threshold: float = 0.95):
        self.threshold = threshold

    async def check(self, data: pd.DataFrame, source: DataSourceConfig) -> QualityCheckConfig:
        completeness = 1 - data.isnull().mean().mean()
        return QualityCheckConfig(
            name=self.get_name(),
            description="Check for data completeness",
            severity=QualityCheckSeverity.ERROR,
            threshold=self.threshold,
            actual_value=float(completeness),
            passed=completeness >= self.threshold,
            source=source
        )

    def get_name(self) -> str:
        return "completeness"