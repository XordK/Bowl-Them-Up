# Generated by Django 4.0 on 2021-12-13 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookings', '0002_player_booking_players'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='BallSize',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='player',
            name='ShoeSize',
            field=models.IntegerField(default=5),
        ),
    ]