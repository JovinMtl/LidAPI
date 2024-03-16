# Generated by Django 5.0.1 on 2024-02-10 09:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0007_trade_date_alter_differente_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="differente",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2024, 2, 10, 11, 16, 51, 424288)
            ),
        ),
        migrations.AlterField(
            model_name="recharge",
            name="date_action",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 2, 10, 11, 16, 51, 423239)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 2, 10, 11, 16, 51, 422057)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 2, 10, 11, 16, 51, 422019)
            ),
        ),
        migrations.AlterField(
            model_name="trade",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2024, 2, 10, 11, 16, 51, 425050)
            ),
        ),
    ]
