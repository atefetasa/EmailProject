from django.db import models
from account_module.models import User, Contact, Signature
from .validators import validate_file_size
import os
from ckeditor.fields import RichTextField


def user_attached_files_path(instance, filename):
    return os.path.join('attached_files', 'user_{0}'.format(instance.sender.username), filename)


class Label(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='labels')
    label_name = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = 'label'
        verbose_name_plural = 'labels'

    def __str__(self):
        return self.label_name


class Email(models.Model):
    title = models.CharField(max_length=225, verbose_name='email title', null=True, blank=True)
    text = RichTextField(null=True, blank=True, verbose_name='email body')
    attached_file = models.FileField(upload_to=user_attached_files_path, null=True, blank=True,
                                     validators=[validate_file_size])
    sender = models.ForeignKey(User, on_delete=models.SET('deleted_account'), related_name='sent_Emails', null=False)
    draft = models.BooleanField(null=False, blank=False)
    direct_receivers = models.ManyToManyField(User, related_name='direct_emails')
    cc_receivers = models.ManyToManyField(User, related_name='cc_emails')
    bcc_receivers = models.ManyToManyField(User, related_name='bcc_emails')
    replied_email = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    deleted_by_user = models.ManyToManyField(User, related_name='deleted_emails')
    labels = models.ManyToManyField(Label, related_name='emails_with_this_label', verbose_name='email_labels')
    signature = models.ForeignKey(Signature, on_delete=models.SET_NULL, null=True, blank=True)
    read_by_user = models.ManyToManyField(User, related_name='read_emails')
    archived_by_user = models.ManyToManyField(User, related_name='archived_emails')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'email'
        verbose_name_plural = 'emails'

    @property
    def file_size(self):
        if self.attached_file and hasattr(self.attached_file, 'size'):
            return self.attached_file.size

    def __str__(self):
        return self.title, self.text, self.direct_receivers, self.cc_receivers, self.bcc_receivers


class ForwardedEmail(models.Model):
    original_email = models.ForeignKey(Email, on_delete=models.CASCADE, null=False, blank=False)
    forwarder = models.ForeignKey(User, on_delete=models.SET('deleted_account'), related_name='forwarded_emails')
    receivers = models.ManyToManyField(User, related_name='received_as_forwarded_emails')

    class Meta:
        verbose_name = 'forwarded email'
        verbose_name_plural = 'forwarded emails'

    def __str__(self):
        return self.original_email.title

