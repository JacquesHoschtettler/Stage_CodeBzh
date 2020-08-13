from django.contrib import admin
from django.contrib.admin import AdminSite

from django.contrib.auth.models import User, Group, Permission


class MyAdminSite(AdminSite):
    site_header = "Administration de l'extranet Sakana Consultants"


class MyAdmin(admin.ModelAdmin):
    pass


admin_site = MyAdminSite(name="SakanaAdmin")
admin_site.register(User)
admin_site.register(Group)
admin_site.register(Permission)
