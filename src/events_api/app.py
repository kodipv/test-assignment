from flask import Flask, g

from events_api.api import api
from events_api.core.project import database


def create_app():
    app = Flask(__name__)
    api.init_app(app)
    configure_hooks(app)
    return app


def configure_hooks(app):
    @app.before_request
    def before_request_func():
        g.uid = 1

    @app.teardown_request
    def teardown_request_func(error=None):
        database.Session.remove()


app = create_app()

if __name__ == "__main__":
    app.run()
