class HTMLReporter(AbstractReporter):
    async def generate(self, report: QualityReportConfig) -> str:
        html = [
            "<html><head><style>",
            "table { border-collapse: collapse; width: 100%; }",
            "th, td { border: 1px solid black; padding: 8px; }",
            "</style></head><body>",
            f"<h1>Quality Report: {report.source.metadata.name}</h1>",
            "<table><tr><th>Check</th><th>Status</th><th>Value</th></tr>"
        ]
        
        for check in report.checks:
            status = "PASSED" if check.passed else "FAILED"
            html.append(
                f"<tr><td>{check.name}</td><td>{status}</td><td>{check.actual_value}</td></tr>"
            )
        
        html.append("</table></body></html>")
        return "\n".join(html)