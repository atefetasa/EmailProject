# Generated by Django 4.2.5 on 2023-10-12 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0007_alter_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtpCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=11, null=True)),
                ('email_address', models.EmailField(blank=True, max_length=300, null=True)),
                ('code', models.PositiveSmallIntegerField()),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
