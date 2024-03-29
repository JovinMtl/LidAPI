# Generated by Django 5.0.1 on 2024-03-21 16:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0019_alter_depotpreuve_date_alter_differente_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="investmentsmade",
            name="approved",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="depotpreuve",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 21, 16, 29, 3, 976045, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="differente",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2024, 3, 21, 18, 29, 3, 973540)
            ),
        ),
        migrations.AlterField(
            model_name="investmentsmade",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 21, 16, 29, 3, 977612, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="investmentsmade",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 21, 16, 29, 3, 977570, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="recharge",
            name="date_action",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 21, 18, 29, 3, 972508)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 21, 18, 29, 3, 971398)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 21, 18, 29, 3, 971360)
            ),
        ),
        migrations.AlterField(
            model_name="retraitlives",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 21, 16, 29, 3, 976822, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="retraitlives",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 21, 16, 29, 3, 976787, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="trade",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2024, 3, 21, 18, 29, 3, 974354)
            ),
        ),
    ]
