from django.contrib import admin
from .models import *
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "id", "number", "prime")

class ShopAdmin(admin.ModelAdmin):
    list_display = ("name", "id", "number", "address", "city", "state", "zipcode", "shop_identity")

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "id", "price", "category", "shop", "approved")

class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer", "id", "transaction_id", "complete", "date_ordered")

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("product", "id", "order", "quantity", "date_added", "packed")

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "nav_bar", "adds")

class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "number", "address",  "city", "state", "zipcode", "id")

admin.site.register(Shop, ShopAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Require)
