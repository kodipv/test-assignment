import factory
from factory.alchemy import SQLAlchemyModelFactory

from events_api.models import Cities, Events, EventsTopics, Topics, Filters, Users
from tests.db_session import TestSession


class BaseFactory(SQLAlchemyModelFactory):
    class Meta:
        sqlalchemy_session = TestSession
        sqlalchemy_session_persistence = "commit"


class CitiesFactory(BaseFactory):
    class Meta:
        model = Cities

    id = factory.Sequence(lambda n: n + 1)
    name = factory.Faker("city")


class TopicsFactory(BaseFactory):
    class Meta:
        model = Topics

    id = factory.Sequence(lambda n: n + 1)
    name = factory.Faker("sentence")


class FiltersFactory(BaseFactory):
    class Meta:
        model = Filters

    id = factory.Sequence(lambda n: n + 1)
    name = factory.Faker("city")


class EventsFactory(BaseFactory):
    class Meta:
        model = Events

    id = factory.Sequence(lambda n: n + 1)
    city_id = factory.Faker("random_int", min=1, max=100, step=1)
    start_date = factory.Faker("future_datetime")
    end_date = factory.Faker("future_datetime")


class EventsTopicsFactory(BaseFactory):
    class Meta:
        model = EventsTopics

    id = factory.Sequence(lambda n: n + 1)
    event_id = factory.Faker("random_int", min=1, max=100, step=1)
    topic_id = factory.Faker("random_int", min=1, max=100, step=1)


class UsersFactory(BaseFactory):
    class Meta:
        model = Users

    id = factory.Sequence(lambda n: n + 1)
    email = factory.Faker("email")
