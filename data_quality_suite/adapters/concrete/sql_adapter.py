from sqlalchemy import create_engine
from ..abstract_adapter import AbstractAdapter

class SQLAdapter(AbstractAdapter):
    def __init__(self, connection_string: str, query: str):
        self.connection_string = connection_string
        self.query = query
        self.engine = None

    async def connect(self) -> None:
        self.engine = create_engine(self.connection_string)

    async def read_data(self) -> pd.DataFrame:
        return pd.read_sql(self.query, self.engine)

    async def get_metadata(self) -> DataSourceConfig:
        return DataSourceConfig(
            catalog_type=CatalogType.HIVE,
            connection_props={"connection_string": self.connection_string},
            metadata=TableMetadata(
                name=self.query.split("FROM")[-1].strip(),
                schema="default",
                catalog="sql",
                format="sql",
                location=self.connection_string,
                properties={}
            )
        )