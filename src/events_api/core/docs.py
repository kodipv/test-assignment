from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin


def resolver(schema):
    return None


spec = APISpec(
    title="events_api",
    version="1.0",
    openapi_version="2.0",
    plugins=[MarshmallowPlugin(schema_name_resolver=resolver)],
)

ma_plugin = spec.plugins.pop()


def as_model(ns, schema):
    response_schema = ma_plugin.resolver.resolve_schema_dict(schema)
    return ns.schema_model(schema.__name__, response_schema)
