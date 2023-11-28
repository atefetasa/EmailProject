from django.shortcuts import render
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView


class CreateMailView(LoginRequiredMixin, TemplateView):
    template_name = 'email_module/compose_email.html'
