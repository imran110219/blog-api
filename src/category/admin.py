from django.contrib import admin

# Register your models here.

from .models import Category

# class CategoryModelAdmin(admin.ModelAdmin):
#     list_display = ["category_name"]
#     class meta:
#         model = Category

admin.site.register(Category)