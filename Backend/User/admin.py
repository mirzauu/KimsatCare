from django.contrib import admin
from .models import CustomUser,  Role, UserRole

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_staff', 'is_superuser']


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ['user', 'role']
