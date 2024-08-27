from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin  import ImportExportModelAdmin

from customers.models import Customer
from users.models import User

# Register your models here.
# admin.site.register(User)
@admin.register(User)
class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'email', 'is_staff')