# Generated by Django 4.2.5 on 2023-11-21 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0019_remove_user_signature_signature'),
        ('email_module', '0006_alter_email_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='reply',
        ),
        migrations.AddField(
            model_name='email',
            name='replied_email',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='email_module.email'),
        ),
        migrations.AddField(
            model_name='email',
            name='signature',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account_module.signature'),
        ),
    ]
