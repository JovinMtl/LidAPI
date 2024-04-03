# Generated by Django 5.0.1 on 2024-04-02 13:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0031_alter_depotpreuve_approved_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="operationstore",
            name="charge",
            field=models.IntegerField(default=0, help_text="La charge de l'operation"),
        ),
        migrations.AlterField(
            model_name="depotpreuve",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 2, 15, 39, 33, 208663)
            ),
        ),
        migrations.AlterField(
            model_name="depotpreuve",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 2, 15, 39, 33, 208594)
            ),
        ),
        migrations.AlterField(
            model_name="differente",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2024, 4, 2, 15, 39, 33, 206094)
            ),
        ),
        migrations.AlterField(
            model_name="investmentsmade",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 2, 15, 39, 33, 210509)
            ),
        ),
        migrations.AlterField(
            model_name="investmentsmade",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 2, 15, 39, 33, 210478)
            ),
        ),
        migrations.AlterField(
            model_name="operationstore",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 2, 15, 39, 33, 212610)
            ),
        ),
        migrations.AlterField(
            model_name="recharge",
            name="date_action",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 2, 15, 39, 33, 205038)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 2, 15, 39, 33, 203949)
            ),
        ),
        migrations.AlterField(
            model_name="requeste",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 2, 15, 39, 33, 203909)
            ),
        ),
        migrations.AlterField(
            model_name="retraitlives",
            name="date_approved",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 4, 2, 13, 39, 33, 209644, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="retraitlives",
            name="date_submitted",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 4, 2, 13, 39, 33, 209606, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="trade",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2024, 4, 2, 15, 39, 33, 206870)
            ),
        ),
    ]