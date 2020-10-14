from marshmallow import Schema, fields

from events_api.api.topics.schema import BaseTopicsSchema


class BaseEventsSchema(Schema):
    city_id = fields.Integer()


class EventsRequestSchema(BaseEventsSchema):
    from_date = fields.Date()
    to_date = fields.Date()
    topics_ids = fields.List(fields.Nested(BaseTopicsSchema))


class EventsResponseSchema(BaseEventsSchema):
    id = fields.Integer(required=True)
    start_date = fields.Date()
    end_date = fields.Date()
    topics = fields.List(fields.Nested(BaseTopicsSchema))


class EventsCreateSchema(BaseEventsSchema):
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    topics_ids = fields.List(fields.Integer)
