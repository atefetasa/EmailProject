# Generated by Django 5.0.2 on 2024-03-13 07:59

import ckeditor.fields
import django.db.models.deletion
import email_module.models
import email_module.validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account_module', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=225, null=True, verbose_name='email title')),
                ('text', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('attached_file', models.FileField(blank=True, null=True, upload_to=email_module.models.user_attached_files_path, validators=[email_module.validators.validate_file_size])),
                ('draft', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('archived_by_user', models.ManyToManyField(blank=True, null=True, related_name='archived_emails', to=settings.AUTH_USER_MODEL)),
                ('bcc_receivers', models.ManyToManyField(blank=True, null=True, related_name='bcc_emails', to=settings.AUTH_USER_MODEL)),
                ('cc_receivers', models.ManyToManyField(blank=True, null=True, related_name='cc_emails', to=settings.AUTH_USER_MODEL)),
                ('deleted_by_user', models.ManyToManyField(blank=True, null=True, related_name='deleted_emails', to=settings.AUTH_USER_MODEL)),
                ('direct_receivers', models.ManyToManyField(blank=True, null=True, related_name='direct_emails', to=settings.AUTH_USER_MODEL)),
                ('read_by_user', models.ManyToManyField(blank=True, null=True, related_name='read_emails', to=settings.AUTH_USER_MODEL)),
                ('replied_email', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='email_module.email')),
                ('sender', models.ForeignKey(on_delete=models.SET('deleted_account'), related_name='sent_Emails', to=settings.AUTH_USER_MODEL)),
                ('signature', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account_module.signature')),
            ],
            options={
                'verbose_name': 'email',
                'verbose_name_plural': 'emails',
            },
        ),
        migrations.CreateModel(
            name='ForwardedEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forwarder', models.ForeignKey(on_delete=models.SET('deleted_account'), related_name='forwarded_emails', to=settings.AUTH_USER_MODEL)),
                ('original_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='email_module.email')),
                ('receivers', models.ManyToManyField(related_name='received_as_forwarded_emails', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'forwarded email',
                'verbose_name_plural': 'forwarded emails',
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_name', models.CharField(max_length=50)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labels', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'label',
                'verbose_name_plural': 'labels',
            },
        ),
        migrations.AddField(
            model_name='email',
            name='labels',
            field=models.ManyToManyField(blank=True, null=True, related_name='emails_with_this_label', to='email_module.label', verbose_name='email_labels'),
        ),
    ]
