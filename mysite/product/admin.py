from django.contrib import admin

# Register your models here.

from product.models import *

admin.site.register(Product)
admin.site.register(Maker_list)
admin.site.register(Cpu_list)
admin.site.register(Ram_list)