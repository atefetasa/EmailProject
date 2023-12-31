# Generated by Django 4.2.5 on 2023-11-23 01:59

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('email_module', '0010_remove_email_deleted_email_remove_email_is_read_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='categories',
        ),
        migrations.AddField(
            model_name='email',
            name='archived_by_user',
            field=models.ManyToManyField(blank=True, related_name='is_archived_by_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='email',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
