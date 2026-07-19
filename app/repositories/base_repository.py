from typing import Generic, TypeVar

from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):
    """
    Base repository that provides access to the database session.
    """

    def __init__(self, db: Session):
        self.db = db