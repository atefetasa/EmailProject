from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin

# first you should add background images and background colors to the database
# you should log in as superuser
# you can add background images in the predefined background images table in database.
# background images and background colors icons that I had added to the database are in the uploads folder in the root directory
# the values you can use as color_name attribute in BackgroundColor table are:
#ffccee
#ffcccc
#ddccff
#ccd9ff
#ffff80
#99ff99
# white


class SiteAppearanceView(LoginRequiredMixin, View):
    login_url = '/account/login/'
    redirect_field_name = None

    def get(self, request):
        site_settings_form = SiteSettingsForm()
        context = {'site_settings_form': site_settings_form}
        return render(request, 'site_module/customize_site_appearance.html', context)

    def post(self, request):
        change_appearance_form = SiteSettingsForm(request.POST)
        if change_appearance_form.is_valid():
            header_background_color = change_appearance_form.cleaned_data.get('header_background_color')
            sidebar_background_color = change_appearance_form.cleaned_data.get('sidebar_background_color')
            main_background_color = change_appearance_form.cleaned_data.get('main_background_color')
            icons_color = change_appearance_form.cleaned_data.get('icons_color')
            background_image = change_appearance_form.cleaned_data.get('background_image')
            user_site_settings = SiteSettings.objects.filter(user__username__iexact=request.user.username).first()
            if user_site_settings:
                user_site_settings.header_background_color = header_background_color
                user_site_settings.sidebar_background_color = sidebar_background_color
                user_site_settings.main_background_color = main_background_color
                user_site_settings.icons_color = icons_color
                user_site_settings.background_image = background_image
                user_site_settings.save()

        return render(request, 'site_module/customize_site_appearance.html',
                      {'site_settings_form': change_appearance_form})


class SiteSettingsView(LoginRequiredMixin, TemplateView):
    login_url = '/account/login/'
    redirect_field_name = None
    template_name = 'site_module/site_settings.html'





