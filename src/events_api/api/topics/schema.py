from marshmallow import Schema, fields


class BaseTopicsSchema(Schema):
    id = fields.Integer()
    name = fields.String()
