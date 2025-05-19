from django.contrib import admin
from .models import Paper

@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('date', 'created_at', 'updated_at')
