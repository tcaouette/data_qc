from typing import Dict, Any
from .abstract_adapter import AbstractAdapter
from .concrete.csv_adapter import CSVAdapter
from .concrete.sql_adapter import SQLAdapter

class AdapterFactory:
    @staticmethod
    def create_adapter(adapter_type: str, config: Dict[str, Any]) -> AbstractAdapter:
        adapters = {
            "csv": CSVAdapter,
            "sql": SQLAdapter
        }
        return adapters[adapter_type](**config)