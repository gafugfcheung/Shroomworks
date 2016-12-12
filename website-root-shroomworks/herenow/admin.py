from django.contrib import admin
from .models import Post, Profile, Location


def deactivate(modeladmin, request, queryset):
    queryset.update(active=False)
deactivate.short_description = "Deactivate selected posts"

def activate(modeladmin, request, queryset):
    queryset.update(active=True)
activate.short_description = "Activate selected posts"

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'caption', 'profile', 'datetime', 'active')
    actions = [deactivate, activate]
admin.site.register(Post, PostAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'status')
admin.site.register(Profile, ProfileAdmin)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'lat', 'lon')
admin.site.register(Location, LocationAdmin)
