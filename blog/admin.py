from django.contrib import admin
from .models import Post, Cosplay

@admin.register(Cosplay)
class CosplayAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category',) # Esto te permitirá filtrar por persona en el admin

admin.site.register(Post)
