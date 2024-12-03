import pandas as pd
from ..abstract_adapter import AbstractAdapter
from ...core.config import DataSourceConfig, TableMetadata, CatalogType
from typing import Dict

class CSVAdapter(AbstractAdapter):
    def __init__(self, filepath: str, options: Dict[str, str] = None):
        self.filepath = filepath
        self.options = options or {}

    async def connect(self) -> None:
        self.df = pd.read_csv(self.filepath, **self.options)

    async def read_data(self) -> pd.DataFrame:
        return self.df

    async def get_metadata(self) -> DataSourceConfig:
        return DataSourceConfig(
            catalog_type=CatalogType.ICEBERG,
            connection_props={"filepath": self.filepath},
            metadata=TableMetadata(
                name=self.filepath.split("/")[-1],
                schema="default",
                catalog="local",
                format="csv",
                location=self.filepath,
                properties=self.options
            )
        )