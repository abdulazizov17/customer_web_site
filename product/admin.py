from django.contrib import admin
from import_export.admin  import ImportExportModelAdmin
from product.models import Product,Category,Image,AttributeValue,ProductAttribute,Attribute

# Register your models her
# admin.site.register(Product)
# admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Attribute)
admin.site.register(AttributeValue)
admin.site.register(ProductAttribute)
@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name', 'price','category')

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

