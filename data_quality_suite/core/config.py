from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional, Union
from pydantic import BaseModel, Field

class CatalogType(str, Enum):
    ICEBERG = "iceberg"
    NESSIE = "nessie"
    POLARIS = "polaris"
    HIVE = "hive"

class QualityCheckSeverity(str, Enum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"

class TableMetadata(BaseModel):
    name: str
    schema: str
    catalog: str
    format: str
    location: str
    properties: Dict[str, str] = Field(default_factory=dict)

class DataSourceConfig(BaseModel):
    catalog_type: CatalogType
    connection_props: Dict[str, str]
    metadata: TableMetadata

class MetricValue(BaseModel):
    metric_name: str
    value: Union[float, int, str]
    timestamp: datetime = Field(default_factory=datetime.now)

class DataProfileConfig(BaseModel):
    source: DataSourceConfig
    metrics: List[MetricValue]
    generated_at: datetime = Field(default_factory=datetime.now)

class QualityCheckConfig(BaseModel):
    name: str
    description: str
    severity: QualityCheckSeverity
    threshold: float
    actual_value: float
    passed: bool
    source: DataSourceConfig

class QualityReportConfig(BaseModel):
    source: DataSourceConfig
    checks: List[QualityCheckConfig]
    profile: Optional[DataProfileConfig]
    generated_at: datetime = Field(default_factory=datetime.now)
