from abc import ABC, abstractmethod
from typing import Any, Dict
from ..core.config import DataSourceConfig

class AbstractAdapter(ABC):
    @abstractmethod
    async def connect(self) -> None:
        pass

    @abstractmethod
    async def read_data(self) -> Any:
        pass

    @abstractmethod
    async def get_metadata(self) -> DataSourceConfig:
        pass