from django.contrib import admin
from django.db import models
# Register your models here.
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','price','stock','category','modified_date','Is_available')
    prepopulated_fields = {'slug':('product_name',)}

admin.site.register(Product,ProductAdmin)