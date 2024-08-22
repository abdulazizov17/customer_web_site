from django.contrib import admin

from product.models import Product,Category,Image,AttributeValue,ProductAttribute,Attribute

# Register your models her
admin.site.register(Product)
admin.site.register(Category)
# admin.site.register(Image)
admin.site.register(Attribute)
admin.site.register(AttributeValue)
admin.site.register(ProductAttribute)

