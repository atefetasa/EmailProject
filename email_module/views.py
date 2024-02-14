from .models import *
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


class CreateMailView(LoginRequiredMixin, TemplateView):
    template_name = 'email_module/compose_email.html'
