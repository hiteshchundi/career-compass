from app.db.models.user import User
from app.db.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.services.base_service import BaseService


class UserService(BaseService[UserRepository]):
    def create_user(self, user: UserCreate) -> User:
        db_user = User(
            name=user.name,
            email=user.email,
        )

        return self.repository.create(db_user)

    def get_user(self, user_id: int) -> User | None:
        return self.repository.get_by_id(user_id)

    def get_user_by_email(self, email: str) -> User | None:
        return self.repository.get_by_email(email)