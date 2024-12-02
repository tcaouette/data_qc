from abc import ABC, abstractmethod
from .config import QualityCheckConfig, DataSourceConfig

class AbstractQualityCheck(ABC):
    @abstractmethod
    async def execute_check(self, data, source: DataSourceConfig) -> QualityCheckConfig:
        pass

    @abstractmethod
    def get_check_name(self) -> str:
        pass
    