# Generated by Django 5.0.1 on 2024-01-25 15:44

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0023_alter_requeste_date_approved_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="requeste",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 25, 17, 44, 41, 412033)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 25, 17, 44, 41, 411995)
            ),
        ),
        migrations.CreateModel(
            name="Recharge",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("phone", models.IntegerField(default=0)),
                ("amount", models.IntegerField(default=0)),
                ("code_transaction", models.CharField(default="xdf", max_length=15)),
                (
                    "date_action",
                    models.DateTimeField(
                        default=datetime.datetime(2024, 1, 25, 17, 44, 41, 413994)
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
