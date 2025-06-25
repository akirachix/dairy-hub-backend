from django.contrib import admin

# Register your models here.
# from .models import Farmer
   
# admin.site.register(Farmer)

from .models import Farmer
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_email', 'phone_number', 'created_at')
    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'
admin.site.register(Farmer, FarmerAdmin)