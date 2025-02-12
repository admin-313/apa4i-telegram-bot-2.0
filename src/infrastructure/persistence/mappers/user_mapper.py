from domain.models.user import User
from domain.models.user_id import UserId
from infrastructure.persistence.models.user_model import UserModel


class UserMapper:
    @staticmethod
    def to_domain(model: UserModel) -> User:
        return User(
            id=UserId(model.id),
            member_since=model.member_since,
            is_superuser=model.is_superuser,
            last_known_name=model.last_known_name,
        )

    @staticmethod
    def to_model(domain: User) -> UserModel:
        return UserModel(
            id=domain.id,
            member_since=domain.member_since,
            is_superuser=domain.is_superuser,
            last_known_name=domain.last_known_name
        )