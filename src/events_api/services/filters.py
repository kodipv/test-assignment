import datetime
from typing import List

from sqlalchemy import and_

from events_api.core.project import database
from events_api.models import Filters


class FiltersService:
    @staticmethod
    def get_filters(
        city_id: int = None,
        topics_ids: List[int] = None,
        start_date: datetime.date = None,
        end_date: datetime.date = None,
    ) -> List[Filters]:
        with database.session() as db_session:
            query = db_session.query(Filters)
            if city_id:
                query = query.filter(Filters.city_id == city_id)
            if topics_ids:
                query = query.filter(Filters.topic_id.in_(topics_ids))
            if start_date:
                query = query.filter(and_(Filters.from_date >= start_date, Filters.to_date <= end_date))
            return query.all()

    @staticmethod
    def create(
            user_id: int,
            city_id: int = None,
            topic_id: int = None,
            from_date: datetime.date = None,
            to_date: datetime.date = None,
    ) -> Filters:
        with database.session() as db_session:
            filters = Filters(
                city_id=city_id,
                topic_id=topic_id,
                from_date=from_date,
                to_date=to_date,
                user_id=user_id,
            )
            db_session.add(filters)
            db_session.commit()
            return filters
