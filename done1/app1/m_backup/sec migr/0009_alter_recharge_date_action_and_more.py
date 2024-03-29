# Generated by Django 5.0.1 on 2024-01-31 12:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0008_alter_recharge_date_action_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recharge",
            name="date_action",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 31, 14, 30, 4, 31076)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 31, 14, 30, 4, 29836)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 31, 14, 30, 4, 29797)
            ),
        ),
    ]
