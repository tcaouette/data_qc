import pandas as pd
from ..abstract_profiler import AbstractProfiler
from ...core.config import DataProfileConfig, MetricValue

class DistributionProfiler(AbstractProfiler):
    async def profile(self, data: pd.DataFrame, source: DataSourceConfig) -> DataProfileConfig:
        metrics = []
        
        for column in data.columns:
            value_counts = data[column].value_counts(normalize=True)
            if not value_counts.empty:
                metrics.extend([
                    MetricValue(
                        metric_name=f"{column}_most_frequent",
                        value=str(value_counts.index[0])
                    ),
                    MetricValue(
                        metric_name=f"{column}_frequency",
                        value=float(value_counts.iloc[0])
                    )
                ])
        
        return DataProfileConfig(source=source, metrics=metrics)