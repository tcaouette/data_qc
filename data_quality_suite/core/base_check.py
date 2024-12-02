from abc import ABC, abstractmethod
from ..core.abstract_check import AbstractQualityCheck
from ..core.config import QualityCheckConfig, DataSourceConfig

class BaseQualityCheck(AbstractQualityCheck):
    def __init__(self, threshold: float):
        self.threshold = threshold

    @abstractmethod
    async def calculate_metric(self, data) -> float:
        pass

    async def execute_check(self, data, source: DataSourceConfig) -> QualityCheckConfig:
        actual_value = await self.calculate_metric(data)
        return QualityCheckConfig(
            name=self.get_check_name(),
            description=self.get_description(),
            severity=self.get_severity(),
            threshold=self.threshold,
            actual_value=actual_value,
            passed=actual_value >= self.threshold,
            source=source
        )

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_severity(self) -> str:
        pass