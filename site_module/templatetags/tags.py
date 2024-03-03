from django import template
from site_module.models import SiteSettings


register = template.Library()


@register.simple_tag
def get_main_background_color(uid):
    site_settings = SiteSettings.objects.filter(user_id__exact=uid).first()
    if not site_settings.main_background_color:
        return "white"
    return site_settings.main_background_color.color_name


@register.simple_tag
def get_main_background_image_url(uid):
    site_settings = SiteSettings.objects.filter(user_id__exact=uid).first()
    if site_settings and site_settings.background_image:
        if site_settings.background_image.image:
            image_path = site_settings.background_image.image.url
            return image_path
        else:
            return None

    return None

