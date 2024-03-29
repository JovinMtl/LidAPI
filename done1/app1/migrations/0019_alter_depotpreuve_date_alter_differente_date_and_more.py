# Generated by Django 5.0.1 on 2024-03-21 16:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0018_investmentsmade_interest_alter_depotpreuve_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="depotpreuve",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 21, 16, 23, 4, 618047, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="differente",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2024, 3, 21, 18, 23, 4, 617072)
            ),
        ),
        migrations.AlterField(
            model_name="investmentsmade",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 21, 16, 23, 4, 618611, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="investmentsmade",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 21, 16, 23, 4, 618596, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="recharge",
            name="date_action",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 21, 18, 23, 4, 616712)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 21, 18, 23, 4, 616333)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 21, 18, 23, 4, 616319)
            ),
        ),
        migrations.AlterField(
            model_name="retraitlives",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 21, 16, 23, 4, 618338, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="retraitlives",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 21, 16, 23, 4, 618317, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="trade",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2024, 3, 21, 18, 23, 4, 617371)
            ),
        ),
    ]
