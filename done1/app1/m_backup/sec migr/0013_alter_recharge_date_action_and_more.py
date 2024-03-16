# Generated by Django 5.0.1 on 2024-01-31 12:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0012_alter_recharge_date_action_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recharge",
            name="date_action",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 31, 14, 56, 48, 976178)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 31, 14, 56, 48, 975790)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 31, 14, 56, 48, 975776)
            ),
        ),
    ]
