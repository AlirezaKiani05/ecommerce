from django.contrib import admin
from .models import Category,Product,Brand  

admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','parent']
    search_fields=['name']
    

