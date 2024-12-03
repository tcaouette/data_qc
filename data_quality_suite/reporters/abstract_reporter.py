from abc import ABC, abstractmethod
from ..core.config import QualityReportConfig

class AbstractReporter(ABC):
    @abstractmethod
    async def generate(self, report: QualityReportConfig) -> str:
        pass