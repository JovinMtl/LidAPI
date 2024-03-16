# Generated by Django 5.0.1 on 2024-03-16 16:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0009_alter_differente_date_alter_recharge_date_action_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="depotpreuve",
            name="owner",
        ),
        migrations.AlterField(
            model_name="depotpreuve",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 16, 18, 7, 14, 733262)
            ),
        ),
        migrations.AlterField(
            model_name="differente",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2024, 3, 16, 18, 7, 14, 732323)
            ),
        ),
        migrations.AlterField(
            model_name="recharge",
            name="date_action",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 16, 18, 7, 14, 731928)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 16, 18, 7, 14, 731515)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 16, 18, 7, 14, 731500)
            ),
        ),
        migrations.AlterField(
            model_name="trade",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2024, 3, 16, 18, 7, 14, 732638)
            ),
        ),
    ]