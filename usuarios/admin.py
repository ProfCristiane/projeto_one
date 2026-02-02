from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Tipo de Usuário', {'fields': ('tipo',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Tipo de Usuário', {'fields': ('tipo',)}),
    )