# Generated by Django 5.0.1 on 2024-01-20 03:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0014_requeste_approved_by_alter_requeste_date_approved_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="requeste",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 20, 5, 55, 8, 747614)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 20, 5, 55, 8, 747576)
            ),
        ),
    ]
