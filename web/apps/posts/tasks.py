from apps.posts.models import SubredditParseConfig
from redditcr.celery import app
import praw
from django.conf import settings

reddit = praw.Reddit(client_id=settings.CLIENT_ID,
                     client_secret=settings.CLIENT_SECRET,
                     password=settings.PASSWORD,
                     user_agent=settings.USER_AGENT,
                     username=settings.USER_NAME)


@app.task()
def crawl_reddit():
    for parse_config in SubredditParseConfig.objects.all():
        for submission in reddit.subreddit(parse_config.name).top('day', limit=parse_config.posts_limit):
            submission_data = {
                'subreddit': parse_config.name,
                'id': submission.name,
                'title': submission.title,
                'url': submission.url,
                'is_self': submission.is_self,
                'self_text': submission.selftext,
                'score': submission.score
            }

            with app.producer_pool.acquire(block=True) as producer:
                producer.publish(
                    submission_data,
                    exchange=settings.EXCHANGE_NAME,
                    routing_key=settings.ROUTING_KEY,
                )
