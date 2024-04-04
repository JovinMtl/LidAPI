# Generated by Django 5.0.1 on 2024-04-04 10:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0047_rateinterestinvestments_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="InterestRateForInvestment",
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
                ("duree", models.CharField(default="1 mois", max_length=8)),
                ("number_month", models.IntegerField(default=1, max_length=15)),
                ("taux", models.FloatField(default=0, max_length=20)),
                (
                    "date_approved",
                    models.DateTimeField(
                        default=datetime.datetime(2024, 4, 4, 12, 46, 19, 829167)
                    ),
                ),
                ("who_approved", models.CharField(default="null", max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name="RateInterestInvestments",
        ),
        migrations.AlterField(
            model_name="commissionforwithdrawal",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 46, 19, 830079)
            ),
        ),
        migrations.AlterField(
            model_name="depotpreuve",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 46, 19, 828050)
            ),
        ),
        migrations.AlterField(
            model_name="depotpreuve",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 46, 19, 828025)
            ),
        ),
        migrations.AlterField(
            model_name="differente",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2024, 4, 4, 12, 46, 19, 827134)
            ),
        ),
        migrations.AlterField(
            model_name="investmentsmade",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 46, 19, 828796)
            ),
        ),
        migrations.AlterField(
            model_name="investmentsmade",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 46, 19, 828783)
            ),
        ),
        migrations.AlterField(
            model_name="operationstore",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 46, 19, 829771)
            ),
        ),
        migrations.AlterField(
            model_name="recharge",
            name="date_action",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 46, 19, 826687)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 46, 19, 826267)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 46, 19, 826252)
            ),
        ),
        migrations.AlterField(
            model_name="retraitlives",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 4, 4, 10, 46, 19, 828374, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="retraitlives",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 4, 4, 10, 46, 19, 828360, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="trade",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2024, 4, 4, 12, 46, 19, 827421)
            ),
        ),
    ]