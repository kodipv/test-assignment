from flask_restplus import Api

from events_api.api.events.resource import ns_events
from events_api.api.filters.resource import ns_filters
from events_api.api.topics.resource import ns_topics

api = Api(title="Events API", description="", doc="/api/docs/")

api.add_namespace(ns_events, path="/events")
api.add_namespace(ns_topics, path="/topics")
api.add_namespace(ns_filters, path="/filters")
