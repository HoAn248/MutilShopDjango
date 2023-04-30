from django.contrib import admin
from .models import Products
# Register your models here.
class PostProduct(admin.ModelAdmin):
    list_display = ['id','name']
    list_filter = ['date']
    search_fields = ['name']
admin.site.register(Products,PostProduct)