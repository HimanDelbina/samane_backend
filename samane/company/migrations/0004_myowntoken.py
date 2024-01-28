# Generated by Django 5.0 on 2023-12-16 13:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_usermodel_is_driver_role_alter_usermodel_is_driver'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyOwnToken',
            fields=[
                ('key', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='Key')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('userTokens', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='auth_token', to='company.usermodel', verbose_name='user_token')),
            ],
            options={
                'verbose_name': 'Users Token',
                'verbose_name_plural': 'User Token',
            },
        ),
    ]