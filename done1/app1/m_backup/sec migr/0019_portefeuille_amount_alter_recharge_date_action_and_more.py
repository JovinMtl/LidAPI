# Generated by Django 5.0.1 on 2024-02-01 07:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0018_alter_recharge_date_action_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="portefeuille",
            name="amount",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="recharge",
            name="date_action",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 2, 1, 9, 9, 32, 37047)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 2, 1, 9, 9, 32, 35852)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 2, 1, 9, 9, 32, 35814)
            ),
        ),
    ]
