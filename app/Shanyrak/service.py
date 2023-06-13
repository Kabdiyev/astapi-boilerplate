from app.config import database
from .repository.repository import PostRepository


class Service:
    def __init__(
        self,
        repository: PostRepository,
    ):
        self.repository = repository


def get_service():
    repository = PostRepository(database)

    svc = Service(repository)
    return svc
