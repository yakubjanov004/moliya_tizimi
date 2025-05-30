from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserModel

class CustomUserAdmin(UserAdmin):
    list_display = ('telefon', 'first_name', 'last_name', 'role')
    list_filter = ('role',)
    search_fields = ('telefon', 'first_name', 'last_name')
    ordering = ('telefon',)
    
    fieldsets = (
        (None, {'fields': ('telefon', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'picture')}),
        ('Permissions', {'fields': ('role',)}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('telefon', 'first_name', 'last_name', 'password1', 'password2', 'role'),
        }),
    )

admin.site.register(UserModel, CustomUserAdmin)
