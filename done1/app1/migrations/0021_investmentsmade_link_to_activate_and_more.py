# Generated by Django 5.0.1 on 2024-03-21 20:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0020_investmentsmade_approved_alter_depotpreuve_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="investmentsmade",
            name="link_to_activate",
            field=models.CharField(
                default="http://127.0.0.1:8002/jov/api/", max_length=50
            ),
        ),
        migrations.AlterField(
            model_name="depotpreuve",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 21, 20, 15, 45, 787657, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="differente",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2024, 3, 21, 22, 15, 45, 784226)
            ),
        ),
        migrations.AlterField(
            model_name="investmentsmade",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 21, 20, 15, 45, 789493, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="investmentsmade",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 21, 20, 15, 45, 789461, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="recharge",
            name="date_action",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 21, 22, 15, 45, 783290)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 21, 22, 15, 45, 781943)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 21, 22, 15, 45, 781901)
            ),
        ),
        migrations.AlterField(
            model_name="retraitlives",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 21, 20, 15, 45, 788493, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="retraitlives",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 21, 20, 15, 45, 788459, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="trade",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2024, 3, 21, 22, 15, 45, 785319)
            ),
        ),
    ]