import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker

from events_api.core.project import config


def init_dramatiq():
    broker = RabbitmqBroker(url=config.rabbitmq.url)
    dramatiq.set_broker(broker)


init_dramatiq()
