# Generated by Django 5.0.1 on 2024-01-29 12:28

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0037_portefeuille_currency_alter_recharge_date_action_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="BiF",
            fields=[
                ("uid", models.IntegerField(primary_key=True, serialize=False)),
                ("lumicash", models.IntegerField(default=0)),
                ("ecocash", models.IntegerField(default=0)),
                ("enoti", models.IntegerField(default=0)),
                ("ihela", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="USD",
            fields=[
                ("uid", models.IntegerField(primary_key=True, serialize=False)),
                ("paypal", models.IntegerField(default=0)),
                ("usdt", models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name="portefeuille",
            name="id",
        ),
        migrations.AlterField(
            model_name="portefeuille",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="recharge",
            name="date_action",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 29, 14, 28, 54, 298824)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 29, 14, 28, 54, 298368)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 29, 14, 28, 54, 298350)
            ),
        ),
    ]
