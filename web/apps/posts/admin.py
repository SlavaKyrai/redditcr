from django.contrib import admin

# Register your models here.
from apps.posts.models import SubredditParseConfig


class SubredditParseConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'translate')


admin.site.register(SubredditParseConfig, SubredditParseConfigAdmin)
