# Generated by Django 5.0.1 on 2024-01-25 17:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0025_alter_recharge_date_action_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="requeste",
            name="code_transaction",
            field=models.CharField(default="xdf", max_length=15),
        ),
        migrations.AlterField(
            model_name="recharge",
            name="date_action",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 25, 19, 14, 50, 929552)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 25, 19, 14, 50, 928391)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 25, 19, 14, 50, 928353)
            ),
        ),
    ]
