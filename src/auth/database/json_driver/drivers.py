import logging
from pathlib import Path
from pydantic import TypeAdapter, ValidationError
from auth.schemas import User
from auth.database.exceptions import (
    WhitelistConfigFileNotFound,
    WhitelistConfigValidationError,
)

USERS_CONFIG_PATH: Path = (
    Path(__file__).parent.parent.parent.parent.parent / "db" / "users.json"
)

logger = logging.getLogger(__name__)


class JSONConfigReader:

    def get_whitelisted_users(self) -> list[User]:
        content: str = self._get_users_db_content()
        user_list_adapter = TypeAdapter(list[User])
        try:
            return user_list_adapter.validate_json(content)

        except ValidationError as ve:
            logger.error(f"Could not validate users config {str(ve)}")
            raise WhitelistConfigValidationError(
                "The config is likely to be empty or contain invalid data"
            )

    def is_in_database(self, user_id: int) -> bool:
        content: list[User] = self.get_whitelisted_users()
        return user_id in [user.id for user in content]

    def _get_users_db_content(self) -> str:
        try:
            return (
                USERS_CONFIG_PATH.read_text()
                .replace("\r", "")
                .replace("\n", "")
                .replace(" ", "")
            )

        except FileNotFoundError:
            logger.critical(f"The users.json config file doesn't seem to exist")
            raise WhitelistConfigFileNotFound(
                "The config file doesn't seem to exist. Have you renamed it to users.json?"
            )


class JSONConfigWriter(JSONConfigReader):

    def add_whitelisted_user(self, user: User) -> User:
        return self._append_user_to_json_db(user)

    def remove_whitelisted_user_by_id_if_exists(self, user_id: int) -> list[User]:
        if self.is_in_database(user_id):
            users: list[User] = self.get_whitelisted_users()
            new_users: list[User] = [usr for usr in users if usr.id != user_id]
            if len(users) != len(new_users):
                self._rewrite_json_db(users=new_users)
                return new_users
        return []

    def demote_if_exists(self, user_id: int) -> User | None:
        if self.is_in_database(user_id):
            old_list: list[User] = self.get_whitelisted_users()

            new_list: list[User] = [
                (
                    User(
                        id=user.id,
                        member_since=user.member_since,
                        is_superuser=False,
                        last_known_name=user.last_known_name,
                    )
                    if user.id == user_id
                    else user
                )
                for user in old_list
            ]
            self._rewrite_json_db(users=new_list)
            return next((user for user in new_list if user.id == user_id), None)

        return None

    def promote_if_exists(self, user_id: int) -> User | None:
        if self.is_in_database(user_id):
            old_list: list[User] = self.get_whitelisted_users()

            new_list: list[User] = [
                (
                    User(
                        id=user.id,
                        member_since=user.member_since,
                        is_superuser=True,
                        last_known_name=user.last_known_name,
                    )
                    if user.id == user_id
                    else user
                )
                for user in old_list
            ]
            self._rewrite_json_db(users=new_list)
            return next((user for user in new_list if user.id == user_id), None)

        return None

    def _append_user_to_json_db(self, user: User) -> User:
        try:
            all_users: list[User] = self.get_whitelisted_users()
            all_users.append(user)
            USERS_CONFIG_PATH.write_bytes(
                TypeAdapter(list[User]).dump_json(all_users, indent=4)
            )

            return user
        except FileNotFoundError:
            logger.critical(f"The users.json config file doesn't seem to exist")
            raise WhitelistConfigFileNotFound(
                "The config file doesn't seem to exist. Have you renamed it to users.json?"
            )

    def _rewrite_json_db(self, users: list[User]) -> list[User]:
        try:
            new_users: list[User] = users
            USERS_CONFIG_PATH.write_bytes(
                TypeAdapter(list[User]).dump_json(new_users, indent=4)
            )
            return new_users
        except FileNotFoundError:
            logger.critical(f"The users.json config file doesn't seem to exist")
            raise WhitelistConfigFileNotFound(
                "The config file doesn't seem to exist. Have you renamed it to users.json?"
            )
