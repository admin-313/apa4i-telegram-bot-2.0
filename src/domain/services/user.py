from datetime import datetime

from domain.models.user import User


class UserService:
    def promote_user(self, user: User) -> None:
        user.is_superuser = True

    def demote_user(self, user: User) -> None:
        user.is_superuser = False

    def create_user(
        self,
        telegram_id: int,
        last_known_name: str | None = None,
        is_superuser: bool = False,
    ) -> User:
        member_since = datetime.now()
        return User(
            id=None,
            telegram_id=telegram_id,
            member_since=member_since,
            is_superuser=is_superuser,
            last_known_name=last_known_name,
        )

    def set_last_known_name(self, user: User, last_known_name: str) -> None:
        user.last_known_name = last_known_name
