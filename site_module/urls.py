from django.urls import path
from . import views

urlpatterns = [
    path('', views.SiteSettingsView.as_view(), name='site_settings_page'),
    path('customize-appearance/', views.SiteAppearanceView.as_view(), name='change_appearance_page'),
]