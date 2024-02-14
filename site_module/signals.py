from .models import SiteSettings
from account_module.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def create_site_settings(sender, instance, created, **kwargs):
    if created:
        SiteSettings.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_site_settings(sender, instance, **kwargs):
    instance.siteSettings.save()
