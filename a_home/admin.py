from django.contrib import admin
from .models import *


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ['name', 'color']
    search_fields = ['name']


admin.site.register(Item, ItemAdmin)
admin.site.register(SiteSetting, SiteSettingAdmin)