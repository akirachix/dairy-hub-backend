from django.contrib import admin

# Register your models here.
from .models import Supplier 

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_email', 'phone_number', 'created_at')
    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'
admin.site.register(Supplier, SupplierAdmin)