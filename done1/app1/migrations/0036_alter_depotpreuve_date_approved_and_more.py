# Generated by Django 5.0.1 on 2024-04-03 08:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0035_alter_depotpreuve_date_approved_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="depotpreuve",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 3, 10, 55, 15, 294444)
            ),
        ),
        migrations.AlterField(
            model_name="depotpreuve",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 3, 10, 55, 15, 294419)
            ),
        ),
        migrations.AlterField(
            model_name="differente",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2024, 4, 3, 10, 55, 15, 293567)
            ),
        ),
        migrations.AlterField(
            model_name="investmentsmade",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 3, 10, 55, 15, 295186)
            ),
        ),
        migrations.AlterField(
            model_name="investmentsmade",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 3, 10, 55, 15, 295122)
            ),
        ),
        migrations.AlterField(
            model_name="operationstore",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 3, 10, 55, 15, 295865)
            ),
        ),
        migrations.AlterField(
            model_name="recharge",
            name="date_action",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 3, 10, 55, 15, 293219)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 3, 10, 55, 15, 292812)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 3, 10, 55, 15, 292797)
            ),
        ),
        migrations.AlterField(
            model_name="retraitlives",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 4, 3, 8, 55, 15, 294781, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="retraitlives",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 4, 3, 8, 55, 15, 294768, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="retraitlives",
            name="owner",
            field=models.CharField(default="null", max_length=10),
        ),
        migrations.AlterField(
            model_name="trade",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2024, 4, 3, 10, 55, 15, 293832)
            ),
        ),
    ]
