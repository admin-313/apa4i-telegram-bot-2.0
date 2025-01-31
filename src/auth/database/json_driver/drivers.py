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

    def add_whitelisted_user(
        self, user: User
    ) -> User:
        json_content: str = user.model_dump_json()
        self._append_to_json_db(json_content)

        return user

    def _append_to_json_db(self, content: str) -> str:
        try:
            with open(USERS_CONFIG_PATH, "a") as json_file:
                json_file.write(content)

            return content
        except FileNotFoundError:
            logger.critical(f"The users.json config file doesn't seem to exist")
            raise WhitelistConfigFileNotFound(
                "The config file doesn't seem to exist. Have you renamed it to users.json?"
            )
