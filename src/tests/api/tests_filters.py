import pytest

from tests.factories import CitiesFactory, TopicsFactory


@pytest.fixture
def base_path():
    return "/filters"


@pytest.mark.usefixtures("clear_all")
class TestFilters:
    def test_create(self, client, base_path):
        city = CitiesFactory.create(id=2)
        topic = TopicsFactory.create(id=2)
        filter_data = {
            "city_id": city.id,
            "topic_id": topic.id,
            "from_date": "2020-11-01",
            "to_date": "2020-11-02",
        }
        resp = client.post("/events", json=filter_data)
        assert resp.status_code == 201
