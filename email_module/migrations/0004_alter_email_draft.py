# Generated by Django 5.0.2 on 2024-03-16 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_module', '0003_alter_email_archived_by_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='draft',
            field=models.BooleanField(),
        ),
    ]
