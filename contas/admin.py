from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from escritorio.models import Escritorio

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('escritorio',)}),
    )
    list_display = UserAdmin.list_display + ('escritorio',)

admin.site.register(CustomUser, CustomUserAdmin)
