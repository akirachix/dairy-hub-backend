from django.contrib import admin

# Register your models here.
<<<<<<< HEAD
from .models import Supplier

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_email', 'phone_number', 'created_at')
    def get_email(self, obj):
        return obj.user.email

    get_email.short_description = 'Email'
    
=======

from .models import Supplier
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_email', 'phone_number', 'created_at')
    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'
>>>>>>> ea98277a3ddd5db0ecc917f01949bdc87b1ce13a
admin.site.register(Supplier, SupplierAdmin)