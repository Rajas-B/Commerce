# Generated by Django 3.0.8 on 2020-07-22 12:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auctions', '0010_watclist'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Watclist',
            new_name='Watchlist',
        ),
    ]
