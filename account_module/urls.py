from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login_page'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('sign-up/', views.RegisterView.as_view(), name='sign_up_page'),
    path('enter-code/', views.EnterCodeView.as_view(), name='enter_code_page'),
    path('enter-code/resend-code/', views.ResendCodeView.as_view(), name='resend_code'),
    path('enter-email/', views.EnterEmailView.as_view(), name='enter_email_page'),
    path('forget-password/', views.ForgetPasswordView.as_view(), name='forget_password_page'),
    path('reset-password/<uidb64>/<token>/', views.ResetPasswordView.as_view(), name='reset_password_page'),
]