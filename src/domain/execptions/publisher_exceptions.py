class PublisherNotFoundException(Exception):
    def __init__(self, publisher_id: str):
        self.publisher_id = publisher_id
        super().__init__(f"Publisher with ID '{publisher_id}' not found.")
