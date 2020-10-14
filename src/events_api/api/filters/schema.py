from marshmallow import Schema, fields


class BaseFiltersSchema(Schema):
    city_id = fields.Integer()
    topic_id = fields.Integer()
    from_date = fields.Date()
    to_date = fields.Date()
