from src.domain.entities.job import Job


def test_job_creation():
    job = Job(id="1", title="Author")
    assert job.id == "1"
    assert job.title == "Author"
