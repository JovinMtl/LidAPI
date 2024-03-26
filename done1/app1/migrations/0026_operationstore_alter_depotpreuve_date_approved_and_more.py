# Generated by Django 5.0.1 on 2024-03-26 11:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0025_alter_depotpreuve_date_approved_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="OperationStore",
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
                ("code", models.CharField(max_length=15, unique=True)),
                ("source", models.CharField(max_length=15)),
                ("destination", models.CharField(default="null", max_length=15)),
                (
                    "amount",
                    models.IntegerField(
                        default=0, help_text="Le montant de l'operation"
                    ),
                ),
                ("motif", models.CharField(max_length=25)),
                (
                    "date_approved",
                    models.DateTimeField(
                        default=datetime.datetime(2024, 3, 26, 13, 28, 17, 438436)
                    ),
                ),
                ("who_approved", models.CharField(default="null", max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name="depotpreuve",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 26, 13, 28, 17, 437040)
            ),
        ),
        migrations.AlterField(
            model_name="depotpreuve",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 26, 13, 28, 17, 437016)
            ),
        ),
        migrations.AlterField(
            model_name="differente",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2024, 3, 26, 13, 28, 17, 436140)
            ),
        ),
        migrations.AlterField(
            model_name="investmentsmade",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 26, 13, 28, 17, 437672)
            ),
        ),
        migrations.AlterField(
            model_name="investmentsmade",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 26, 13, 28, 17, 437662)
            ),
        ),
        migrations.AlterField(
            model_name="recharge",
            name="date_action",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 26, 13, 28, 17, 435779)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 26, 13, 28, 17, 435398)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 26, 13, 28, 17, 435382)
            ),
        ),
        migrations.AlterField(
            model_name="retraitlives",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 26, 11, 28, 17, 437377, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="retraitlives",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 26, 11, 28, 17, 437362, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="trade",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2024, 3, 26, 13, 28, 17, 436421)
            ),
        ),
    ]
