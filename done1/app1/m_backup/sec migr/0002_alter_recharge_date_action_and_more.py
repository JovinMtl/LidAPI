# Generated by Django 5.0.1 on 2024-01-31 11:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recharge",
            name="date_action",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 31, 13, 22, 11, 549507)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 31, 13, 22, 11, 548388)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 31, 13, 22, 11, 548352)
            ),
        ),
    ]
