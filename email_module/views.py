from .models import *
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import *


class CreateMailView(LoginRequiredMixin, CreateView):
    login_url = '/account/login/'
    redirect_field_name = None
    model = Email
    form_class = CreateEmailForm
    template_name = 'email_module/compose_email.html'
    success_url = reverse_lazy('home_page')

    def get_form_kwargs(self):
        kwargs = super(CreateMailView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def post(self, request, *args, **kwargs):
        key_word_arguments = self.get_form_kwargs()
        form = self.form_class(request.POST, request=key_word_arguments.get('request'))
        if form.is_valid():
            email_title = form.cleaned_data.get('title')
            email_text = form.cleaned_data.get('text')
            email_attachment = form.cleaned_data.get('attached_file')
            email_sender = request.user
            selected_direct_receivers = form.cleaned_data.get('direct_receivers')
            selected_cc_receivers = form.cleaned_data.get('cc_receivers')
            selected_bcc_receivers = form.cleaned_data.get('bcc_receivers')
            draft = form.cleaned_data.get('draft')
            selected_labels = form.cleaned_data.get('labels')
            selected_signature = form.cleaned_data.get('signature')
            new_email = self.model.objects.create(sender=email_sender, title=email_title, text=email_text,
                                                  attached_file=email_attachment, draft=draft)
            if selected_labels:
                new_email.labels.set(selected_labels)
            if selected_signature:
                new_email.signature = selected_signature

            if selected_direct_receivers:
                selected_direct_receivers_list = selected_direct_receivers.split(',')
                if selected_direct_receivers_list[-1] == '':
                    selected_direct_receivers_list.pop(-1)

                for selected_direct_receiver in selected_direct_receivers_list:
                    to = User.objects.get(username__iexact=selected_direct_receiver)
                    if not to:
                        form.add_error('to', f'user with "{selected_direct_receiver}" username does not exist.')
                        return self.form_invalid(form)

                    new_email.direct_receivers.add(to)

            if selected_cc_receivers:
                selected_cc_receivers_list = selected_cc_receivers.split(',')
                if selected_cc_receivers_list[-1] == '':
                    selected_cc_receivers_list.pop(-1)

                for selected_cc_receiver in selected_cc_receivers_list:
                    cc = User.objects.get(username__iexact=selected_cc_receiver)
                    if not cc:
                        form.add_error('cc', f'user with "{selected_cc_receiver}" username does not exist.')
                        return self.form_invalid(form)

                    new_email.cc_receivers.add(cc)

            if selected_bcc_receivers:
                selected_bcc_receivers_list = selected_bcc_receivers.split(',')
                if selected_bcc_receivers_list[-1] == '':
                    selected_bcc_receivers_list.pop(-1)

                for selected_bcc_receiver in selected_bcc_receivers_list:
                    bcc = User.objects.get(username__iexact=selected_bcc_receiver)
                    if not bcc:
                        form.add_error('bcc', f'user with "{selected_bcc_receiver}" username does not exist.')
                        return self.form_invalid(form)

                    new_email.bcc_receivers.add(bcc)

            return super(CreateMailView, self).post(request, *args, **kwargs)

        return super(CreateMailView, self).form_invalid(form)
