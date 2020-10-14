from flask_restplus import Resource, Namespace
from webargs.flaskparser import use_kwargs

from events_api.api.events.schema import EventsRequestSchema, EventsCreateSchema, EventsResponseSchema
from events_api.core.docs import as_model
from events_api.services.events import EventsService
from events_api.tasks.notification import notify_users_of_new_event

ns_events = Namespace("events", description="Events")


@ns_events.route("")
class EventsResource(Resource):
    @ns_events.doc(expect=[as_model(ns_events, EventsRequestSchema)])
    @ns_events.doc(responses={200: ("Success", as_model(ns_events, EventsResponseSchema))})
    @use_kwargs(EventsRequestSchema, location="query")
    def get(self, **kwargs):
        events = EventsService.get(**kwargs)
        result = EventsResponseSchema(many=True).dump(events)
        return {"items": result}

    @ns_events.doc(expect=[as_model(ns_events, EventsCreateSchema)])
    @ns_events.doc(responses={200: ("Success", as_model(ns_events, EventsResponseSchema))})
    @use_kwargs(EventsCreateSchema, location="json")
    def post(self, city_id, topics_ids, start_date, end_date):
        event = EventsService.create(city_id, start_date, end_date)
        if event:
            notify_users_of_new_event.send(
                city_id,
                topics_ids,
                start_date.strftime("%Y-%m-%d"),
                end_date.strftime("%Y-%m-%d")
            ),
            EventsService.bind_topics_to_event(event.id, topics_ids)
            result = EventsResponseSchema().dump(event)
            return {"data": result}, 201
        else:
            return "Internal error", 500
