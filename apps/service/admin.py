from django.contrib import admin
from .models import OylikHisobot, EskirishShablon, Work

@admin.register(OylikHisobot)
class OylikHisobotAdmin(admin.ModelAdmin):
    list_display = ('sana', 'fio', 'ish_haqi', 'create_at', 'update_at')
    search_fields = ('fio',)
    list_filter = ('create_at', 'update_at')

@admin.register(EskirishShablon)
class EskirishShablonAdmin(admin.ModelAdmin):
    list_display = ('sana', 'nomi', 'summa', 'create_at', 'update_at')
    search_fields = ('nomi',)
    list_filter = ('create_at', 'update_at')

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'narxi', 'create_at', 'update_at')
    search_fields = ('nomi',)
    list_filter = ('create_at', 'update_at')
