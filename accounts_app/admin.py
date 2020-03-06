from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from accounts_app.forms import CustomUserChangeForm, AdminUserCreationForm
from django.utils.translation import gettext_lazy as _

from accounts_app.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('email',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = ((None, {'classes': ('wide',), 'fields': ('username', 'email', 'password1', 'password2'), }),)
    form = CustomUserChangeForm
    add_form = AdminUserCreationForm
    list_display = ('username', 'email', 'is_staff')
    search_fields = ('username', 'email')
    ordering = ('username',)
