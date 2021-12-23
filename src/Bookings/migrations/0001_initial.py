# Generated by Django 3.2.9 on 2021-12-22 21:02

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
            name='LaneModel',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Available', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='BookingModel',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('DateTime', models.DateTimeField()),
                ('NumberOfPlayers', models.IntegerField()),
                ('CustomerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('LaneId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bookings.lanemodel')),
            ],
        ),
    ]
