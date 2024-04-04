# Generated by Django 5.0.1 on 2024-04-04 10:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0045_alter_commissionforwithdrawal_date_approved_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="commissionforwithdrawal",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 27, 2, 971633)
            ),
        ),
        migrations.AlterField(
            model_name="depotpreuve",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 27, 2, 966315)
            ),
        ),
        migrations.AlterField(
            model_name="depotpreuve",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 27, 2, 966242)
            ),
        ),
        migrations.AlterField(
            model_name="differente",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2024, 4, 4, 12, 27, 2, 963649)
            ),
        ),
        migrations.AlterField(
            model_name="investmentsmade",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 27, 2, 968565)
            ),
        ),
        migrations.AlterField(
            model_name="investmentsmade",
            name="date_deadline",
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name="investmentsmade",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 27, 2, 968381)
            ),
        ),
        migrations.AlterField(
            model_name="operationstore",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 27, 2, 970663)
            ),
        ),
        migrations.AlterField(
            model_name="recharge",
            name="date_action",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 27, 2, 962562)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 27, 2, 961444)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 4, 12, 27, 2, 961406)
            ),
        ),
        migrations.AlterField(
            model_name="retraitlives",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 4, 4, 10, 27, 2, 967354, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="retraitlives",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 4, 4, 10, 27, 2, 967316, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="trade",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2024, 4, 4, 12, 27, 2, 964484)
            ),
        ),
    ]
