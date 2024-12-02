from abc import ABC, abstractmethod
from .config import DataProfileConfig, DataSourceConfig

class AbstractProfile(ABC):
    @abstractmethod
    async def create_profile(self, data, source: DataSourceConfig) -> DataProfileConfig:
        pass