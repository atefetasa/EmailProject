from django.urls import path
from .views import *

urlpatterns = [
    path('compose/', CreateMailView.as_view(), name='compose_mail_page'),
    path('add-label/', AddNewLabelView.as_view(), name='add_new_label_page'),
]

