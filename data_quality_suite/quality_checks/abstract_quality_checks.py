from abc import ABC, abstractmethod
from typing import Any
from ..core.config import QualityCheckConfig, DataSourceConfig

class AbstractQualityCheck(ABC):
    @abstractmethod
    async def check(self, data: Any, source: DataSourceConfig) -> QualityCheckConfig:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass