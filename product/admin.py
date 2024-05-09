from django.contrib import admin
from .models import Product, Variation


class VariationInLine(admin.TabularInline):
    model = Variation
    extra = 1


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
    inlines = [VariationInLine,]


@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    list_display = 'id', 'name'
    list_display_links = 'name', 
