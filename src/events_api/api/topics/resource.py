from flask_restplus import Resource, Namespace
from webargs.flaskparser import use_kwargs

from events_api.api.topics.schema import BaseTopicsSchema
from events_api.core.docs import as_model
from events_api.services.topics import TopicsService

ns_topics = Namespace("topics", description="Topics")


@ns_topics.route("")
class TopicsResource(Resource):
    @ns_topics.doc(expect=[as_model(ns_topics, BaseTopicsSchema)])
    @ns_topics.doc(responses={200: ("Success", as_model(ns_topics, BaseTopicsSchema))})
    @use_kwargs(BaseTopicsSchema, location="json")
    def post(self, **kwargs):
        topic = TopicsService.create(**kwargs)
        result = BaseTopicsSchema().dump(topic)
        return {"data": result}, 201
