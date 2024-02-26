from .forms import *
from .models import User, OtpCode, PasswordHistory
from django.utils import timezone
from django.http import Http404
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_str, force_bytes
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.views import View
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from .utils import *


class RegisterView(View):
    def get(self, request):
        register_form = RegisterModelForm()
        context = {'register_form': register_form}
        return render(request, 'account_module/register.html', context)

    def post(self, request):
        register_form = RegisterModelForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password = register_form.cleaned_data.get('password')
            recovery_email = register_form.cleaned_data.get('email')
            phone_number = register_form.cleaned_data.get('phone_number')
            user = User.objects.create_user(username=username, password=password,
                                            email=recovery_email, phone_number=phone_number)
            password_history = PasswordHistory.objects.create(user=user, password=password)
            password_history.save()
            otp_code = OtpCode.objects.create(user=user)
            otp_code.generate_code()
            is_sent, message = send_otp_code(otp_code=otp_code, email_address=recovery_email, phone_number=phone_number)
            if is_sent:
                messages.success(request, message)
            elif not is_sent:
                messages.error(request, message)

            request.session['user_registration_info'] = {
                'username': user.username,
                'recovery_email': user.email,
                'phone_number': user.phone_number
            }

            # this session is only valid for one hour
            request.session.set_expiry(3600)
            return redirect(reverse('enter_code_page'))

        return render(request, 'account_module/register.html', {'register_form': register_form})


class EnterCodeView(FormView):
    template_name = 'account_module/enter_code.html'
    form_class = EnterCodeForm
    success_url = '/account/login/'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        if "resend_status" in request.session:
            resend_status = request.session.get('resend_status')
            context = {
                'form': form,
                'message': resend_status['message'],
                'color': resend_status['color']
            }
        else:
            context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user_information = request.session.get('user_registration_info')
            otp_object = OtpCode.objects.filter(user__username__iexact=user_information['username']).latest('created_at')
            entered_code = self.request.POST.get('code')
            current_time = timezone.now()
            remained_time = current_time - otp_object.created_at
            if entered_code != otp_object.code:
                form.add_error('code', 'The entered cod is incorrect. please try again')
                return self.form_invalid(form)

            if remained_time.total_seconds() > 240:
                form.add_error('code', 'the expiration of your code has been passed')
                return self.form_invalid(form)

            user = User.objects.get(username__iexact=user_information['username'])
            user.is_active = True
            user.save()
            messages.success(request, "your account has been successfully activated")
            return super(EnterCodeView, self).form_valid(form)

        return super(EnterCodeView, self).form_invalid(form)


class ResendCodeView(View):
    def post(self, request):
        user_information = request.session.get('user_registration_info')
        users_last_otp = OtpCode.objects.filter(user__username__iexact=user_information['username']).latest(
            'created_at')
        current_time = timezone.now()
        passed_time = (current_time - users_last_otp.created_at).total_seconds()
        if passed_time < 240:
            request.session['resend_status'] = {
                'message': "The code has been already sent to you. please check your email",
                'color': "red"
            }
        else:
            user = User.objects.filter(username__iexact=user_information['username']).first()
            otp_code = OtpCode.objects.create(user=user)
            otp_code.generate_code()
            is_sent, message = send_otp_code(otp_code=otp_code, email_address=user_information['recovery_email'],
                                             phone_number=user_information['phone_number'])
            if is_sent:
                request.session['resend_status'] = {
                    'message': message,
                    'color': 'green'
                }
            elif not is_sent:
                request.session['resend_status'] = {
                    'message': message,
                    'color': 'red'
                }

        request.session.set_expiry(900)
        return redirect(reverse('enter_code_page'))


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('home_page'))

        login_form = LoginForm()
        context = {'login_form': login_form}
        return render(request, 'account_module/login.html', context)

    def post(self, request):
        login_form = LoginForm(request.POST)
        context = {
            'login_form': login_form
        }
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(username__iexact=username).first()
            if user:
                if user.is_active:
                    is_password_correct = user.check_password(password)
                    if is_password_correct:
                        login(request, user)
                        messages.success(request, 'you have logged in successfully')
                        return redirect(reverse('home_page'))
                    else:
                        messages.error(request, 'entered username or password is incorrect')
                        login_form.add_error('username', 'entered username or password is incorrect')
                        login_form.add_error('password', 'entered username or password is incorrect')
                else:
                    context['activate_button'] = True
                    login_form.add_error('username', 'your account is not activated. '
                                                     'activate it by clicking the button bellow')
            else:
                messages.error(request, 'entered username or password is incorrect')

        return render(request, 'account_module/login.html', context)


class EnterEmailView(View):
    def get(self, request):
        email_form = EnterEmailForm()
        context = {'email_form': email_form, 'enter_email_page': True}
        return render(request, 'account_module/enter_email.html', context)

    def post(self, request):
        email_form = EnterEmailForm(request.POST)
        if email_form.is_valid():
            email = email_form.cleaned_data.get('recovery_email')
            user: User = User.objects.filter(email__iexact=email).first()
            if user:
                otp_code = OtpCode.objects.create(user=user)
                otp_code.generate_code()
                is_sent, message = send_otp_code(otp_code=otp_code, email_address=email,
                                                 phone_number=None)
                if is_sent:
                    messages.success(request, message)
                    return redirect(reverse('enter_code_page'))

                elif not is_sent:
                    messages.error(request, message)
            else:
                email_form.add_error('recovery_email', """There is no user with this email in system.
                 please enter the email once you have entered at register time""")

        return render(request, 'account_module/enter_email.html', {'email_form': email_form, 'enter_email_page': True})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('home_page'))


class ForgetPasswordView(View):
    def get(self, request):
        forget_pass_form = EnterEmailForm()
        context = {'forget_pass_form': forget_pass_form, 'forget_password_page': True}
        return render(request, 'account_module/enter_email.html', context)

    def post(self, request):
        forget_pass_form = EnterEmailForm(request.POST)
        success_count = 0
        if forget_pass_form.is_valid():
            email = forget_pass_form.cleaned_data.get('recovery_email')
            user: User = User.objects.filter(email__iexact=email).first()
            if user:
                current_site = get_current_site(request)
                reset_password_token = PasswordResetTokenGenerator()
                html_message = render_to_string(
                    'account_module/reset_password_email.html', {
                        'user': user,
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': reset_password_token.make_token(user)
                    })
                success_count = send_mail(subject='reset password', message='', from_email='atefe1376tasa613@gmail.com',
                                          recipient_list=[email], html_message=html_message)
            else:
                forget_pass_form.add_error('recovery_email', """There is no user with this email in system.
                                 please enter the email once you have entered at register time""")

        if success_count == 1:
            success_message = 'reset password link has been successfully sent to your email'
            context = {'forget_pass_form': forget_pass_form, 'forget_password_page': True,
                       'success_message': success_message}
            return render(request, 'account_module/enter_email.html', context)

        elif success_count == 0:
            raise Http404("the password reset emil has been not successfully sent to you. please try again.")


class ResetPasswordView(FormView):
    form_class = ResetPasswordForm
    template_name = 'account_module/reset_password.html'
    success_url = '/account/login/'

    def get_context_data(self, **kwargs):
        context = super(ResetPasswordView, self).get_context_data(**kwargs)
        context['uid'] = self.kwargs['uidb64']
        context['token'] = self.kwargs['token']
        return context

    def get(self, request, *args, **kwargs):
        uid = force_str(s=urlsafe_base64_decode(self.kwargs['uidb64']).decode(), strings_only=True)
        user = User.objects.filter(pk=uid).first()
        if user and PasswordResetTokenGenerator().check_token(user, self.kwargs['token']):
            return super().get(request, *args, **kwargs)
        else:
            raise Http404("Invalid reset link")

    def form_valid(self, form):
        context = self.get_context_data()
        encoded_uid = context['uid']
        pk = force_str(s=urlsafe_base64_decode(encoded_uid).decode(), strings_only=True)
        user = User.objects.filter(pk=pk).first()
        if user:
            user_previous_passwords = user.previous_passwords.all()
            if user_previous_passwords:
                for previous_password in list(user_previous_passwords):
                    pattern = create_pattern(str(previous_password))
                    if bool(pattern.search(form.cleaned_data.get('password'))):
                        form.add_error('password',
                                       "this password is similar to previous one. please pick another password")
                        return super(ResetPasswordView, self).form_invalid(form)

            user.set_password(form.cleaned_data.get('password'))
            user.save()
            password_history = PasswordHistory.objects.create(user=user, password=form.cleaned_data.get('password'))
            password_history.save()
            messages.success(self.request, 'your password has been successfully changed')
            return super().form_valid(form)
        else:
            raise Http404("Invalid Reset link")

    def post(self, request, *args, **kwargs):
        return super(ResetPasswordView, self).post(request, *args, **kwargs)

