# Generated by Django 5.0 on 2024-01-09 17:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("company", "0014_drivermodel_is_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="drivermodel",
            name="is_accept",
            field=models.BooleanField(default=False, verbose_name="تاییدیه نهایی"),
        ),
    ]
