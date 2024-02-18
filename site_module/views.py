from django.shortcuts import render
from .models import SiteSettings
from django.views import View
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin


class SiteSettingsView(View, LoginRequiredMixin):
    def get(self, request):
        site_settings_form = SiteSettingsForm()
        context = {'site_settings_form': site_settings_form}
        return render(request, 'site_module/site_settings.html', context)

    def post(self, request):
        pass

