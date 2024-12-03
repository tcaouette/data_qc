from ..abstract_check import AbstractQualityCheck
from ...core.config import QualityCheckConfig, QualityCheckSeverity

class ConsistencyCheck(AbstractQualityCheck):
    def __init__(self, rules: Dict[str, str], threshold: float = 0.95):
        self.rules = rules
        self.threshold = threshold

    async def check(self, data: pd.DataFrame, source: DataSourceConfig) -> QualityCheckConfig:
        consistencies = []
        for column, pattern in self.rules.items():
            if column in data.columns:
                matches = data[column].str.match(pattern, na=False)
                consistencies.append(matches.mean())
        
        consistency_score = sum(consistencies) / len(consistencies) if consistencies else 0
        return QualityCheckConfig(
            name=self.get_name(),
            description="Check for data format consistency",
            severity=QualityCheckSeverity.WARNING,
            threshold=self.threshold,
            actual_value=float(consistency_score),
            passed=consistency_score >= self.threshold,
            source=source
        )

    def get_name(self) -> str:
        return "consistency"