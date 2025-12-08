from src.domain.entities.job import Job


class JobMapper:
    @staticmethod
    def from_dict(data: dict) -> Job:
        return Job(
            id=data["id"],
            title=data["title"],
        )