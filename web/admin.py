from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "title",
    )
    prepopulated_fields = {"slug": ("title",)}