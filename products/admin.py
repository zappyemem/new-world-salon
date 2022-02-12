from django.contrib import admin
from .models import Product, Category, Review
from .forms import ReviewForm

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)


class ReviewAdmin(admin.ModelAdmin):
    form = ReviewForm
    list_display = (
        'text',
        'product',
        'user',
        'created_at',
    )
        
    ordering = ('created_at', )

admin.site.register(Review, ReviewAdmin) 
