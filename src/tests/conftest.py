import contextlib
from unittest.mock import MagicMock

import dramatiq
import pytest
from dramatiq import Worker
from dramatiq.brokers.stub import StubBroker
from sqlalchemy import MetaData, Table

from events_api import tasks
from events_api.app import create_app
from events_api.core.project import database

broker = StubBroker()
broker.emit_after("process_boot")


def clear_tables(engine, table_list=None):
    meta = MetaData()
    with contextlib.closing(engine.connect()) as con:
        trans = con.begin()
        if table_list is None:
            meta.reflect(bind=engine)
            for table in reversed(meta.sorted_tables):
                con.execute(table.delete())
        else:
            for table_name in table_list:
                table = Table(table_name, meta, autoload=True, autoload_with=engine)
                con.execute(table.delete())
        trans.commit()


@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    return app.test_client()


@pytest.fixture(scope="function")
def clear_all():
    yield
    clear_tables(database.db_engine, table_list=["events_topics"])
    clear_tables(database.db_engine, table_list=["topics"])
    clear_tables(database.db_engine, table_list=["events"])
    clear_tables(database.db_engine, table_list=["cities"])
    clear_tables(database.db_engine, table_list=["filters"])


@pytest.fixture(scope="session")
def tear_down_db_session():
    yield
    database.Session.remove()


@pytest.fixture(scope="session")
def stub_broker():
    tasks.init_dramatiq = MagicMock()
    broker.flush_all()
    dramatiq.set_broker(broker)
    yield broker


@pytest.fixture
def stub_worker():
    worker = Worker(broker, worker_timeout=100)
    worker.start()
    yield worker
    worker.stop()
