from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'displayname', 'info']
    search_fields = ['user__username', 'displayname', 'info']
    list_filter = ['user__is_active', 'user__is_staff', 'user__is_superuser']
    ordering = ['user__username']


admin.site.register(Profile, ProfileAdmin)
