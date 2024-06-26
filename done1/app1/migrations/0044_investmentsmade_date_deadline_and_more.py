# Generated by Django 5.0.1 on 2024-04-04 10:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0043_investmentsmade_code_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="investmentsmade",
            name="date_deadline",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 23, 23, 176840)
            ),
        ),
        migrations.AlterField(
            model_name="commissionforwithdrawal",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 23, 23, 179744)
            ),
        ),
        migrations.AlterField(
            model_name="depotpreuve",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 23, 23, 174409)
            ),
        ),
        migrations.AlterField(
            model_name="depotpreuve",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 23, 23, 174284)
            ),
        ),
        migrations.AlterField(
            model_name="differente",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2024, 4, 4, 12, 23, 23, 171327)
            ),
        ),
        migrations.AlterField(
            model_name="investmentsmade",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 23, 23, 176813)
            ),
        ),
        migrations.AlterField(
            model_name="investmentsmade",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 23, 23, 176633)
            ),
        ),
        migrations.AlterField(
            model_name="operationstore",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 23, 23, 178863)
            ),
        ),
        migrations.AlterField(
            model_name="recharge",
            name="date_action",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 23, 23, 170190)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 23, 23, 169050)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 23, 23, 169012)
            ),
        ),
        migrations.AlterField(
            model_name="retraitlives",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 4, 4, 10, 23, 23, 175635, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="retraitlives",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 4, 4, 10, 23, 23, 175594, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="trade",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2024, 4, 4, 12, 23, 23, 172127)
            ),
        ),
    ]
