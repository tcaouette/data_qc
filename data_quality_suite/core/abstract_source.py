from abc import ABC, abstractmethod
from .config import DataSourceConfig

class AbstractDataSource(ABC):
    @abstractmethod
    async def get_metadata(self) -> DataSourceConfig:
        pass

    @abstractmethod
    async def read_data(self):
        pass