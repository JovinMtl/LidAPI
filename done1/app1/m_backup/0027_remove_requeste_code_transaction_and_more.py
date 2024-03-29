# Generated by Django 5.0.1 on 2024-01-25 17:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0026_requeste_code_transaction_alter_recharge_date_action_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="requeste",
            name="code_transaction",
        ),
        migrations.AlterField(
            model_name="recharge",
            name="date_action",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 25, 19, 18, 6, 942517)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 25, 19, 18, 6, 941386)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 25, 19, 18, 6, 941348)
            ),
        ),
    ]
