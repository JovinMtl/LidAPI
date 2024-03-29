# Generated by Django 5.0.1 on 2024-01-29 13:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0041_delete_bif_remove_currency_paymethods_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recharge",
            name="date_action",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 29, 15, 25, 31, 114810)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 29, 15, 25, 31, 113526)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 29, 15, 25, 31, 113487)
            ),
        ),
    ]
