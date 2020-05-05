from django.contrib import admin
from .models import Category, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'category',)
    search_fields = ('title',)
    list_filter = ('category',)


admin.site.register(Category)
