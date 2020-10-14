import pytest

from tests.factories import CitiesFactory, TopicsFactory, EventsTopicsFactory, EventsFactory


@pytest.fixture
def base_path():
    return "/events"


@pytest.mark.usefixtures("clear_all")
class TestEvents:
    def test_create(self, client, base_path):
        city = CitiesFactory.create()
        topic = TopicsFactory.create()
        event_data = {
            "city_id": city.id,
            "topics_ids": [topic.id],
            "start_date": "2020-11-01",
            "end_date": "2020-11-02",
        }
        resp = client.post(base_path, json=event_data)
        assert resp.status_code == 201

    def test_get_all(self, client, base_path):
        city = CitiesFactory.create()
        topic = TopicsFactory.create()
        event = EventsFactory.create(city_id=city.id)
        EventsTopicsFactory.create(topic_id=topic.id, event_id=event.id)
        resp = client.get(f"{base_path}")
        assert resp.status_code == 200
        assert len(resp.json["items"]) == 1

    def test_get_by_city(self, client, base_path):
        city1 = CitiesFactory.create()
        city2 = CitiesFactory.create()
        topic = TopicsFactory.create()
        EventsFactory.create(city_id=city1.id)
        event = EventsFactory.create(city_id=city2.id)
        EventsTopicsFactory.create(topic_id=topic.id, event_id=event.id)
        resp = client.get(f"{base_path}?city_id={city2.id}")
        assert resp.status_code == 200
        assert len(resp.json["items"]) == 1
        assert resp.json["items"][0]["id"] == event.id
