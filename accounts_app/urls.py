from django.urls import path

from accounts_app import views

app_name = 'accounts'

urlpatterns = [
    path('create/', views.UserCreateView.as_view(), name='create')
]
