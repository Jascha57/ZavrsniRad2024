from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.models import Group

class GroupAdmin(admin.ModelAdmin):
    pass

class GroupProxy(Group):
    class Meta:
        proxy = True
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

admin.site.register(CustomUser)
admin.site.unregister(Group)
admin.site.register(GroupProxy, GroupAdmin)