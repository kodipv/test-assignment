import os
from contextlib import contextmanager
from dataclasses import dataclass

from sqlalchemy.engine import Engine, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from .config import LocalConfig, DockerConfig

current_config = DockerConfig if os.environ["CONFIG_LEVEL"] == "docker" else LocalConfig


@dataclass
class RabbitmqConfig:
    host: str
    port: int
    user: str
    password: str
    vhost: str = ""

    @property
    def url(self) -> str:
        return f"amqp://{self.user}:{self.password}@{self.host}:{self.port}/{self.vhost}"


@dataclass
class DbConfig:
    host: str
    port: int
    user: str
    password: str
    database: str

    @property
    def dsn(self) -> str:
        return f"postgresql://{self.user}:{self.password}@{self.host}:{str(self.port)}/{self.database}"


def create_app_engine() -> Engine:
    db_config = DbConfig(**current_config.database)
    engine = create_engine(db_config.dsn)
    return engine


class Database:
    def __init__(self):
        self.db_engine = create_app_engine()
        self.Session = scoped_session(sessionmaker(bind=self.db_engine))

    @contextmanager
    def session(self):
        s = self.Session()
        try:
            yield s
        except Exception:
            s.rollback()
            raise


class Config:
    def __init__(self):
        self.database = Database()
        self.rabbitmq = RabbitmqConfig(**current_config.rabbitmq)


database = Database()
config = Config()
