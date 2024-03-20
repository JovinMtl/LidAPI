# Generated by Django 5.0.1 on 2024-03-20 09:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0010_remove_depotpreuve_owner_alter_depotpreuve_date_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="RetraitLives",
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
                ("currency", models.CharField(default="null", max_length=10)),
                ("numero", models.CharField(default="numerovide", max_length=25)),
                ("benefitor", models.CharField(default="nulldeposant", max_length=25)),
                (
                    "montant",
                    models.IntegerField(
                        default=0, help_text="Le montant que vous deposez"
                    ),
                ),
                (
                    "date_submitted",
                    models.DateTimeField(
                        default=datetime.datetime(2024, 3, 20, 11, 55, 35, 156231)
                    ),
                ),
                (
                    "date_approved",
                    models.DateTimeField(
                        default=datetime.datetime(2024, 3, 20, 11, 55, 35, 156242)
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="depotpreuve",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 20, 11, 55, 35, 155959)
            ),
        ),
        migrations.AlterField(
            model_name="differente",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2024, 3, 20, 11, 55, 35, 155079)
            ),
        ),
        migrations.AlterField(
            model_name="recharge",
            name="date_action",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 20, 11, 55, 35, 154728)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 20, 11, 55, 35, 154290)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 20, 11, 55, 35, 154276)
            ),
        ),
        migrations.AlterField(
            model_name="trade",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2024, 3, 20, 11, 55, 35, 155378)
            ),
        ),
    ]