from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name',
        'marketing_price',
        'promotional_marketing_pricing'
    ]
    list_display_links = 'id', 'name'
    list_per_page = 10
    ordering = 'name',
    search_fields = 'name',
    prepopulated_fields = {
        'slug': ('name',),
    }
