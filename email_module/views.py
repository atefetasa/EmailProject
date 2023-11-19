from django.shortcuts import render
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView


class CreateMail(LoginRequiredMixin, CreateView):
    pass
