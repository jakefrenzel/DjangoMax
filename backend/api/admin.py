from django.contrib import admin
from .models import Item, Box, Product, Setting


# Register your example models here.
admin.site.register(Item)
admin.site.register(Box)
admin.site.register(Product)


# Register official models
admin.site.register(Setting)
