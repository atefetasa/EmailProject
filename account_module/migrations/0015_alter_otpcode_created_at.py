# Generated by Django 4.2.5 on 2023-10-22 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0014_otpcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpcode',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]