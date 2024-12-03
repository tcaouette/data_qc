import pandas as pd
from ..abstract_profiler import AbstractProfiler
from ...core.config import DataProfileConfig, MetricValue

class StatisticalProfiler(AbstractProfiler):
    async def profile(self, data: pd.DataFrame, source: DataSourceConfig) -> DataProfileConfig:
        metrics = []
        
        for column in data.select_dtypes(include=['number']).columns:
            stats = data[column].describe()
            metrics.extend([
                MetricValue(metric_name=f"{column}_mean", value=float(stats['mean'])),
                MetricValue(metric_name=f"{column}_std", value=float(stats['std'])),
                MetricValue(metric_name=f"{column}_min", value=float(stats['min'])),
                MetricValue(metric_name=f"{column}_max", value=float(stats['max']))
            ])
        
        return DataProfileConfig(source=source, metrics=metrics)