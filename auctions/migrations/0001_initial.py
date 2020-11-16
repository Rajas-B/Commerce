# Generated by Django 3.0.8 on 2020-07-18 11:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.SmallIntegerField()),
                ('description', models.TextField()),
                ('image', models.URLField(max_length=500)),
                ('baseprice', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('closedate', models.DateField(blank=True, null=True)),
                ('active', models.BooleanField()),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auctioneer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
