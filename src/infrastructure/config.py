from dataclasses import dataclass
from pathlib import Path


@dataclass
class DatabaseConfig:
    url: str

    @classmethod
    def default_sqlite(cls) -> "DatabaseConfig":
        db_path = Path(__file__).parents[2] / "data" / "db.sqlite3"
        return cls(url=f"sqlite+aiosqlite:///{db_path}")
