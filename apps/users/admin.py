from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from apps.users.models import User


class UserAdmin(BaseUserAdmin):
    model = User

    list_display = (
        'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser', 'created_at'
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('-created_at',)
    change_password_form = auth_admin.AdminPasswordChangeForm

    readonly_fields = ('created_at', 'updated_at')


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
