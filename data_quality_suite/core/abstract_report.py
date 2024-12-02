from abc import ABC, abstractmethod
from .config import QualityReportConfig

class AbstractReport(ABC):
    @abstractmethod
    async def generate(self, report: QualityReportConfig) -> str:
        pass