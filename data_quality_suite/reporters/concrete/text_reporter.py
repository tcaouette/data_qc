class TextReporter(AbstractReporter):
    async def generate(self, report: QualityReportConfig) -> str:
        lines = [
            f"Quality Report for {report.source.metadata.name}",
            f"Generated at: {report.generated_at}",
            "\nQuality Checks:"
        ]
        
        for check in report.checks:
            lines.extend([
                f"- {check.name}: {'PASSED' if check.passed else 'FAILED'}",
                f"  Threshold: {check.threshold}, Actual: {check.actual_value}"
            ])
        
        return "\n".join(lines)