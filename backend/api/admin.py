from django.contrib import admin
from .models import Item, Box, Product, Setting, Facility, Franchisee


# Register your example models here.
admin.site.register(Item)
admin.site.register(Box)
admin.site.register(Product)


# Register official models
admin.site.register(Setting)
admin.site.register(Facility)
admin.site.register(Franchisee)