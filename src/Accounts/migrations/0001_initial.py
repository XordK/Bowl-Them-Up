# Generated by Django 4.0 on 2021-12-09 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('UserID', models.AutoField(primary_key=True, serialize=False)),
                ('FirstName', models.TextField(max_length=64)),
                ('LastName', models.TextField(max_length=64)),
                ('PhoneNumber', models.TextField(max_length=10)),
                ('EmailAddress', models.TextField(max_length=128)),
                ('Password', models.TextField(max_length=64)),
            ],
        ),
    ]