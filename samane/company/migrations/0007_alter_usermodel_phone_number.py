# Generated by Django 5.0 on 2023-12-30 12:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("company", "0006_usermodel_company_code_alter_usermodel_is_tell"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usermodel",
            name="phone_number",
            field=models.CharField(max_length=11, verbose_name="شماره موبایل"),
        ),
    ]