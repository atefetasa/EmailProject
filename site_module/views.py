from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin


class SiteAppearanceView(LoginRequiredMixin, View):
    login_url = '/account/login/'
    redirect_field_name = None

    def get(self, request):
        site_settings_form = SiteSettingsForm()
        context = {'site_settings_form': site_settings_form}
        return render(request, 'site_module/customize_site_appearance.html', context)

    def post(self, request):
        pass


class SiteSettingsView(LoginRequiredMixin, TemplateView):
    login_url = '/account/login/'
    redirect_field_name = None
    template_name = 'site_module/site_settings.html'





