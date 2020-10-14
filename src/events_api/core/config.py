class DockerConfig:
    database = {
        "host": "db",
        "port": 5432,
        "user": "user",
        "password": "password",
        "database": "events_api"
    }
    rabbitmq = {
        "host": "rabbitmq",
        "port": 5672,
        "user": "user",
        "password": "password",
        "vhost": "events_api"
    }


class LocalConfig:
    database = {
        "host": "127.0.0.1",
        "port": 5432,
        "user": "user",
        "password": "password",
        "database": "events_api"
    }
    rabbitmq = {
        "host": "127.0.0.1",
        "port": 5672,
        "user": "user",
        "password": "password",
        "vhost": "events_api"
    }
