# Generated by Django 5.0.1 on 2024-03-23 14:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0023_investmentsmade_owner_investmentsmade_who_approved_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="depotpreuve",
            name="date",
        ),
        migrations.AddField(
            model_name="depotpreuve",
            name="approved",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="depotpreuve",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 23, 16, 30, 28, 498770)
            ),
        ),
        migrations.AddField(
            model_name="depotpreuve",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 23, 16, 30, 28, 498705)
            ),
        ),
        migrations.AddField(
            model_name="depotpreuve",
            name="link_to_approve",
            field=models.URLField(
                default="http://127.0.0.1:8002/jov/api/", max_length=50
            ),
        ),
        migrations.AddField(
            model_name="depotpreuve",
            name="owner",
            field=models.CharField(default="null", max_length=10),
        ),
        migrations.AddField(
            model_name="depotpreuve",
            name="who_approved",
            field=models.CharField(default="null", max_length=10),
        ),
        migrations.AlterField(
            model_name="differente",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2024, 3, 23, 16, 30, 28, 496156)
            ),
        ),
        migrations.AlterField(
            model_name="investmentsmade",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 23, 16, 30, 28, 500766)
            ),
        ),
        migrations.AlterField(
            model_name="investmentsmade",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 23, 16, 30, 28, 500737)
            ),
        ),
        migrations.AlterField(
            model_name="recharge",
            name="date_action",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 23, 16, 30, 28, 495387)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 23, 16, 30, 28, 494157)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 23, 16, 30, 28, 494117)
            ),
        ),
        migrations.AlterField(
            model_name="retraitlives",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 23, 14, 30, 28, 499943, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="retraitlives",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 23, 14, 30, 28, 499905, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="trade",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2024, 3, 23, 16, 30, 28, 496908)
            ),
        ),
    ]
