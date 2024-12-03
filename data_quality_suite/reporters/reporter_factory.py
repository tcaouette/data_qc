class ReporterFactory:
    @staticmethod
    def create_reporter(reporter_type: str) -> AbstractReporter:
        reporters = {
            "text": TextReporter,
            "json": JSONReporter,
            "html": HTMLReporter
        }
        return reporters[reporter_type]()