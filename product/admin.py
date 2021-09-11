from django.contrib import admin

from .models import Category, Color, Product, Collection

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Color)
admin.site.register(Collection)
