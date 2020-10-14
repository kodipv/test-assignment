from sqlalchemy import Column, Integer, Text, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Users(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True)
    email = Column("email", Text, nullable=False)


class Cities(Base):
    __tablename__ = "cities"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", Text, nullable=False)


class Topics(Base):
    __tablename__ = "topics"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", Text, nullable=False)


class Events(Base):
    __tablename__ = "events"

    id = Column("id", Integer, primary_key=True)
    city_id = Column("city_id", Integer, ForeignKey("cities.id"), nullable=False)
    start_date = Column("start_date", Date, nullable=False)
    end_date = Column("end_date", Date, nullable=False)

    topics = relationship(
        "Topics",
        secondary="events_topics",
        primaryjoin="Events.id == EventsTopics.event_id",
        secondaryjoin="EventsTopics.topic_id == Topics.id",
    )


class EventsTopics(Base):
    __tablename__ = "events_topics"

    id = Column("id", Integer, primary_key=True)
    event_id = Column("event_id", Integer, ForeignKey("events.id"), nullable=False)
    topic_id = Column("topic_id", Integer, ForeignKey("topics.id"), nullable=False)


class Filters(Base):
    __tablename__ = "filters"

    id = Column("id", Integer, primary_key=True)
    city_id = Column("city_id", Integer)
    topic_id = Column("topic_id", Integer)
    from_date = Column("from_date", Date)
    to_date = Column("to_date", Date)
    user_id = Column("user_id", Integer, ForeignKey("users.id"))
