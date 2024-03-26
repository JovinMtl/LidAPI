# Generated by Django 5.0.1 on 2024-03-26 11:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0026_operationstore_alter_depotpreuve_date_approved_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="operationstore",
            name="currency",
            field=models.CharField(default="null", max_length=10),
        ),
        migrations.AlterField(
            model_name="depotpreuve",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 26, 13, 41, 58, 971840)
            ),
        ),
        migrations.AlterField(
            model_name="depotpreuve",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 26, 13, 41, 58, 971772)
            ),
        ),
        migrations.AlterField(
            model_name="differente",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2024, 3, 26, 13, 41, 58, 969247)
            ),
        ),
        migrations.AlterField(
            model_name="investmentsmade",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 26, 13, 41, 58, 973648)
            ),
        ),
        migrations.AlterField(
            model_name="investmentsmade",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 26, 13, 41, 58, 973619)
            ),
        ),
        migrations.AlterField(
            model_name="operationstore",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 26, 13, 41, 58, 975772)
            ),
        ),
        migrations.AlterField(
            model_name="recharge",
            name="date_action",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 26, 13, 41, 58, 968223)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 26, 13, 41, 58, 967113)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 26, 13, 41, 58, 967072)
            ),
        ),
        migrations.AlterField(
            model_name="retraitlives",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 26, 11, 41, 58, 972798, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="retraitlives",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 26, 11, 41, 58, 972758, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="trade",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2024, 3, 26, 13, 41, 58, 970098)
            ),
        ),
    ]
