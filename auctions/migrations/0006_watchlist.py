# Generated by Django 3.0.8 on 2020-07-21 15:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auctions', '0005_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.Product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_watchlist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
