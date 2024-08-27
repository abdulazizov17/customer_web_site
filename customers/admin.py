from django.contrib import admin
from .models import Customer
from django.utils.html import mark_safe
from django.contrib.auth.models import User, Group
from import_export.admin  import ImportExportModelAdmin

# admin.site.register(Customer)
admin.site.unregister(Group)

@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email','image','joined')
    search_fields = ('first_name', 'last_name', 'email','image')
    list_filter = ('last_name', 'email')

    def image_tag(self, obj):
        if obj.image:
            return mark_safe('<img src="%s" width="50" height="50" />' % obj.image.url)
        return 'No Image'

    image_tag.short_description = 'Image'

