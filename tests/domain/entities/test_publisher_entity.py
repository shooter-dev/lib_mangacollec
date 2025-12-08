from src.domain.entities.publisher import Publisher


def test_publisher_creation():
    publisher = Publisher(
        id="1",
        title="Pika",
        closed=False,
        editions_count=10,
        no_amazon=False,
    )
    assert publisher.id == "1"
    assert publisher.title == "Pika"
    assert not publisher.closed
    assert publisher.editions_count == 10
    assert not publisher.no_amazon
