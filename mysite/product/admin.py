from django.contrib import admin

# Register your models here.

from product.models import *

admin.site.register(Product)
admin.site.register(Maker_list)
admin.site.register(Cpu_list)
admin.site.register(Ram_list)


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'tag_list')

#     def get_queryset(self, request):
#         return super().get_queryset(request).prefetch_related('tags')

#     def tag_list(self, obj):
#         return ', '.join(o.name for o in obj.tags.all())
