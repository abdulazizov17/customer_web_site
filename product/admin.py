from django.contrib import admin

from product.models import Product,Category,Image

# Register your models her
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Image)