from events_api.core.project import database
from events_api.models import Topics


class TopicsService:
    @staticmethod
    def create(name: str) -> Topics:
        with database.session() as db_session:
            topic = Topics(name=name)
            db_session.add(topic)
            db_session.commit()
            return topic
