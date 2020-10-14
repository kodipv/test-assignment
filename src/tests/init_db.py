from events_api.models import Base
from tests.db_session import engine
from tests.factories import UsersFactory, CitiesFactory, TopicsFactory

Base.metadata.drop_all(bind=engine)
print("Tables have been dropped!")
Base.metadata.create_all(bind=engine)
print("Tables have been created!")

UsersFactory.create()
CitiesFactory.create()
TopicsFactory.create()
