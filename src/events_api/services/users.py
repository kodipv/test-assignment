from typing import List

from events_api.core.project import database
from events_api.models import Users


class UsersService:
    @staticmethod
    def get_by_ids(ids: List[int]) -> List[Users]:
        with database.session() as db_session:
            return db_session.query(Users).filter(Users.id.in_(ids)).all()
