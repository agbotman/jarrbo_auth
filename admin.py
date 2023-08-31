from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')  # whatever
    search_fields = ('first_name', 'last_name')

admin.site.register(User, UserAdmin)