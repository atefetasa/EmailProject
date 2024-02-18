from django.urls import path
from . import views

urlpatterns = [
    path('site-settings/', views.SiteSettingsView.as_view(), name='site_settings_page'),
]