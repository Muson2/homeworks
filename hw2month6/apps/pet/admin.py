from django.contrib import admin
from .models import CustomUser, Pet

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'role', 'is_staff')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Pet)