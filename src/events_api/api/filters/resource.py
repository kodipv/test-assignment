from flask import g
from flask_restplus import Resource, Namespace
from webargs.flaskparser import use_kwargs

from events_api.api.filters.schema import BaseFiltersSchema
from events_api.core.docs import as_model
from events_api.services.filters import FiltersService

ns_filters = Namespace("filters", description="Filters")


@ns_filters.route("")
class FiltersResource(Resource):
    @ns_filters.doc(expect=[as_model(ns_filters, BaseFiltersSchema)])
    @ns_filters.doc(responses={200: ("Success", as_model(ns_filters, BaseFiltersSchema))})
    @use_kwargs(BaseFiltersSchema, location="json")
    def post(self, **kwargs):
        filter_ = FiltersService.create(g.uid, **kwargs)
        result = BaseFiltersSchema().dump(filter_)
        return {"data": result}, 201
