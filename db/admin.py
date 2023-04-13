from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from db.models import Customer, Order, OrderItem, Product, User

admin.site.register(User, UserAdmin)
admin.site.register(Customer)
admin.site.register(OrderItem)
admin.site.register(Product)
admin.site.register(Order)
