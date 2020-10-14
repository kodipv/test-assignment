from typing import List

from sqlalchemy import and_
from sqlalchemy.orm.strategy_options import contains_eager

from events_api.core.project import database
from events_api.models import Events, EventsTopics


class EventsService:
    @staticmethod
    def get(
        city_id: int = None,
        topic_id: int = None,
        from_date: bool = False,
        to_date: bool = False,
    ) -> List[Events]:
        with database.session() as db_session:
            query = db_session.query(Events).outerjoin(Events.topics)
            if topic_id:
                query = query.options(contains_eager(Events.topics)).filter(Events.id == topic_id)
            if city_id:
                query = query.filter(Events.city_id == city_id)
            if from_date and to_date:
                query = query.filter(and_(Events.start_date >= to_date, Events.end_date <= to_date))
            return query.all()

    @staticmethod
    def create(city_id, start_date, end_date) -> Events:
        with database.session() as db_session:
            events = Events(
                city_id=city_id,
                start_date=start_date,
                end_date=end_date,
            )
            db_session.add(events)
            db_session.commit()
            return events

    @staticmethod
    def bind_topics_to_event(event_id, topics_ids: List[int]):
        with database.session() as db_session:
            for topic_id in topics_ids:
                event_topic = EventsTopics(event_id=event_id,topic_id=topic_id,)
                db_session.add(event_topic)
            db_session.commit()
