from django.contrib import admin

# Register your models here.

from product.models import Maker_list, Product

admin.site.register(Product)
admin.site.register(Maker_list)