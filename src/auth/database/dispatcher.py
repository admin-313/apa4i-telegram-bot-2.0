from typing import Any
from auth.database.json_driver.drivers import JSONConfigReader, JSONConfigWriter

database_service_dispatcher: dict[str, Any] = {
    "json_readonly": JSONConfigReader,
    "json_admin_only_writer": JSONConfigWriter
}