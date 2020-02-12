from django.urls import path

from base_app import views

name = 'base'

urlpatterns = [
    path('', views.top, name='top')
]
