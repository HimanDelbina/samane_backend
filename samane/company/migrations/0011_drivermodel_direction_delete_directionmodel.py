# Generated by Django 5.0 on 2024-01-05 14:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("company", "0010_directionmodel"),
    ]

    operations = [
        migrations.AddField(
            model_name="drivermodel",
            name="direction",
            field=models.CharField(
                choices=[("R", "آمدن به شرکت"), ("W", "برگشت از شرکت")],
                default="",
                max_length=1,
                verbose_name="مسیر",
            ),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name="DirectionModel",
        ),
    ]
