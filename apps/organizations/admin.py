from django.contrib import admin
from .models import Korxona

@admin.register(Korxona)
class KorxonaAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'create_at', 'update_at')
    search_fields = ('nomi',)
    list_filter = ('create_at', 'update_at')