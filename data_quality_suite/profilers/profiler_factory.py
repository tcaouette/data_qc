class ProfilerFactory:
    @staticmethod
    def create_profiler(profiler_type: str) -> AbstractProfiler:
        profilers = {
            "statistical": StatisticalProfiler,
            "distribution": DistributionProfiler
        }
        return profilers[profiler_type]()