from django.shortcuts import render
from account_module.models import User
from site_module.models import SiteSettings
from django.contrib.auth.decorators import login_required


def home_view(request):
    return render(request, 'home_module/home.html', {})


def site_header_partial(request):
    if request.user.is_authenticated:
        settings: SiteSettings = SiteSettings.objects.filter(user__username__iexact=request.user.username).first()
        context = {
            'header_background_color': settings.header_background_color,
            'icons_color': settings.icons_color
        }
    else:
        context = {
            'header_background_color': "#f3ccff",
            'icons_color': "c"
        }

    return render(request, 'shared/site_header_partial.html', context)


def site_sidebar_partial(request):
    if request.user.is_authenticated:
        settings: SiteSettings = SiteSettings.objects.filter(user__username__iexact=request.user.username).first()
        context = {
            'sidebar_background_color': settings.sidebar_background_color,
            'icons_color': settings.icons_color
        }
    else:
        context = {
            'sidebar_background_color': "white",
            'icons_color': "c"
        }

    return render(request, 'shared/site_sidebar_partial.html', context)




