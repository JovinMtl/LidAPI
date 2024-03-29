# Generated by Django 5.0.1 on 2024-01-26 13:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0029_alter_recharge_date_action_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recharge",
            name="date_action",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 26, 15, 38, 32, 807666)
            ),
        ),
        migrations.AlterField(
            model_name="recharge",
            name="phone",
            field=models.CharField(default="61999999", max_length=12),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 26, 15, 38, 32, 806578)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 26, 15, 38, 32, 806540)
            ),
        ),
    ]
