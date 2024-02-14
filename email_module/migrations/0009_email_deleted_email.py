# Generated by Django 4.2.5 on 2023-11-22 00:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('email_module', '0008_email_is_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='deleted_email',
            field=models.ManyToManyField(blank=True, related_name='deleted_emails', to=settings.AUTH_USER_MODEL),
        ),
    ]
