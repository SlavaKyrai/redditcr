# Generated by Django 3.0.5 on 2020-05-01 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubredditParseConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('translate', models.BooleanField(default=False)),
                ('posts_limit', models.IntegerField(default=10)),
            ],
        ),
    ]
