from typing import List

import dramatiq

from events_api.services.users import UsersService
from events_api.services.filters import FiltersService


@dramatiq.actor(max_retries=0)
def notify_users_of_new_event(city_id, topics_ids: List[int], start_date, end_date):
    print("Start notifying users of new event...")
    filters = FiltersService.get_filters(city_id, topics_ids, start_date, end_date)
    users = UsersService.get_by_ids([filter_.user_id for filter_ in filters])
    for user in users:
        print(f"Send notification to {user.email} about event that takes place in {city_id}")
