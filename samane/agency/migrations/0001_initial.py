# Generated by Django 5.0.1 on 2024-01-29 06:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0017_usermodel_agency'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgencyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='نام آژانس')),
            ],
            options={
                'verbose_name': 'آژانس ',
                'verbose_name_plural': ' آژانس ها',
            },
        ),
        migrations.CreateModel(
            name='AgencyUserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.CharField(choices=[('R', 'آمدن به شرکت'), ('W', 'برگشت از شرکت')], max_length=1, verbose_name='مسیر')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agency', to='agency.agencymodel', verbose_name='آژانس')),
                ('users', models.ManyToManyField(to='company.usermodel', verbose_name='کاربران')),
            ],
            options={
                'verbose_name': 'ثبت آزانس ',
                'verbose_name_plural': ' ثبت آژانس ها',
            },
        ),
    ]
