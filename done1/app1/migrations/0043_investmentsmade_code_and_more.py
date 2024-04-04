# Generated by Django 5.0.1 on 2024-04-04 09:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0042_alter_commissionforwithdrawal_date_approved_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="investmentsmade",
            name="code",
            field=models.CharField(default="null", max_length=10),
        ),
        migrations.AlterField(
            model_name="commissionforwithdrawal",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 11, 52, 6, 730707)
            ),
        ),
        migrations.AlterField(
            model_name="depotpreuve",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 11, 52, 6, 725345)
            ),
        ),
        migrations.AlterField(
            model_name="depotpreuve",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 11, 52, 6, 725238)
            ),
        ),
        migrations.AlterField(
            model_name="differente",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2024, 4, 4, 11, 52, 6, 722412)
            ),
        ),
        migrations.AlterField(
            model_name="investmentsmade",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 11, 52, 6, 727907)
            ),
        ),
        migrations.AlterField(
            model_name="investmentsmade",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 11, 52, 6, 727876)
            ),
        ),
        migrations.AlterField(
            model_name="operationstore",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 11, 52, 6, 729839)
            ),
        ),
        migrations.AlterField(
            model_name="recharge",
            name="date_action",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 11, 52, 6, 721631)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 11, 52, 6, 720479)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 11, 52, 6, 720440)
            ),
        ),
        migrations.AlterField(
            model_name="retraitlives",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 4, 4, 9, 52, 6, 726853, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="retraitlives",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 4, 4, 9, 52, 6, 726805, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="trade",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2024, 4, 4, 11, 52, 6, 723237)
            ),
        ),
    ]