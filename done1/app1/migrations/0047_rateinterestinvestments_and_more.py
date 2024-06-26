# Generated by Django 5.0.1 on 2024-04-04 10:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0046_alter_commissionforwithdrawal_date_approved_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="RateInterestInvestments",
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
                        default=datetime.datetime(2024, 4, 4, 12, 42, 14, 309196)
                    ),
                ),
                ("who_approved", models.CharField(default="null", max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name="commissionforwithdrawal",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 42, 14, 310098)
            ),
        ),
        migrations.AlterField(
            model_name="depotpreuve",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 42, 14, 308121)
            ),
        ),
        migrations.AlterField(
            model_name="depotpreuve",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 42, 14, 308096)
            ),
        ),
        migrations.AlterField(
            model_name="differente",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2024, 4, 4, 12, 42, 14, 307221)
            ),
        ),
        migrations.AlterField(
            model_name="investmentsmade",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 42, 14, 308833)
            ),
        ),
        migrations.AlterField(
            model_name="investmentsmade",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 42, 14, 308821)
            ),
        ),
        migrations.AlterField(
            model_name="operationstore",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 42, 14, 309794)
            ),
        ),
        migrations.AlterField(
            model_name="recharge",
            name="date_action",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 42, 14, 306866)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 42, 14, 306434)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 42, 14, 306420)
            ),
        ),
        migrations.AlterField(
            model_name="retraitlives",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 4, 4, 10, 42, 14, 308438, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="retraitlives",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 4, 4, 10, 42, 14, 308422, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="trade",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2024, 4, 4, 12, 42, 14, 307494)
            ),
        ),
    ]
