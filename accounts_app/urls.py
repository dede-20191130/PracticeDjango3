from django.contrib.auth import views as auth_views
from django.urls import path

from accounts_app import views
from accounts_app.forms import CustomAuthenticationForm

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(form_class=CustomAuthenticationForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('create/', views.UserCreateView.as_view(), name='create'),
    path('profile/', views.UserProfileView.as_view(), name="profile"),
    path('change/', views.UserChangeView.as_view(), name="change"),
]
