class QualityCheckFactory:
    @staticmethod
    def create_check(check_type: str, config: Dict[str, Any]) -> AbstractQualityCheck:
        checks = {
            "completeness": CompletenessCheck,
            "consistency": ConsistencyCheck
        }
        return checks[check_type](**config)