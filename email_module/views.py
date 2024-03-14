from .models import *
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import *


class CreateMailView(LoginRequiredMixin, View):
    def get(self, request):
        form = CreateEmailForm(user=request.user)
        context = {
            'form': form
        }
        return render(request, 'email_module/compose_email.html', context)

    def post(self, request):
        form = CreateEmailForm(request.POST)
        if form.is_valid():
            email_title = form.cleaned_data.get('title')
            email_text = form.cleaned_data.get('text')
            email_attachment = form.cleaned_data.get('attachment')
            email_sender = request.user
            direct_receivers = form.cleaned_data.get('to')
            cc_receivers = form.cleaned_data.get('cc')
            bcc_receivers = form.cleaned_data.get('bcc')
            draft = form.cleaned_data.get('is_draft')
            labels = form.cleaned_data.get('labels')
            signature = form.cleaned_data.get('signature')
            return HttpResponse("form submitted successfully")
        else:
            return render(request, 'email_module/compose_email.html', {'form': form})

