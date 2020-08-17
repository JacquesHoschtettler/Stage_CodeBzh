from django.contrib import admin

from django.contrib.auth.models import Permission

from .models import ExtensionUser


class MyExtensionAdmin(admin.ModelAdmin):
    list_display = ['user', 'nb_trials']


admin.site.register(Permission)
admin.site.register(ExtensionUser, MyExtensionAdmin)
