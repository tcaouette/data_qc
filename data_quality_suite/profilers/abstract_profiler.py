from abc import ABC, abstractmethod
from typing import Any
from ..core.config import DataProfileConfig, DataSourceConfig

class AbstractProfiler(ABC):
    @abstractmethod
    async def profile(self, data: Any, source: DataSourceConfig) -> DataProfileConfig:
        pass
