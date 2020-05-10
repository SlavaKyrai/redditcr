from django.db import models


class SubredditParseConfig(models.Model):
    name = models.CharField(max_length=40)
    translate = models.BooleanField(default=False)
    posts_limit = models.IntegerField(default=10)
