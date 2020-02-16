from django.urls import path
from django.views.generic import TemplateView

from base_app import views

app_name = 'base'

urlpatterns = [
    path('', views.TopView.as_view(), name='top'),
    path('terms/', TemplateView.as_view(template_name='base_app/terms.html'), name='terms'),
]
