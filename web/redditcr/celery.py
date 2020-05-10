from __future__ import absolute_import, unicode_literals

import os

import kombu
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'redditcr.settings')

app = Celery('redditcr')


app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


with app.pool.acquire(block=True) as conn:
    exchange = kombu.Exchange(
        name='reddit_exchange',
        type='direct',
        durable=True,
        channel=conn,
    )
    exchange.declare()

    queue = kombu.Queue(
        name='reddit_queue',
        exchange=exchange,
        routing_key='reddit',
        channel=conn,
        message_ttl=600,
        queue_arguments={
            'x-queue-type': 'classic'
        },
        durable=True
    )
    queue.declare()
