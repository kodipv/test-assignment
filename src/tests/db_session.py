from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from events_api.core.project import DbConfig, current_config


def create_db_engine():
    db_config = DbConfig(**current_config.database)
    engine = create_engine(db_config.dsn)
    return engine


engine = create_db_engine()
TestSession = scoped_session(sessionmaker(bind=engine))
