from django.contrib import admin
from .models import Item, Box, Product, Setting, Facility, Franchisee, User, MembershipTier, Membership, Court, Booking


# Register your example models here.
admin.site.register(Item)
admin.site.register(Box)
admin.site.register(Product)


# Register official models
admin.site.register(Setting)
admin.site.register(Facility)
admin.site.register(Franchisee)
admin.site.register(User)
admin.site.register(MembershipTier)
admin.site.register(Membership)
admin.site.register(Court)
admin.site.register(Booking)