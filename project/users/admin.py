from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.models import Group

class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser

    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active',)
    search_fields = ('email', 'first_name', 'last_name',)
    exclude = ('password',)

    def has_add_permission(self, request):
        return False

class GroupAdmin(admin.ModelAdmin):
    pass

class GroupProxy(Group):
    class Meta:
        proxy = True
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)
admin.site.register(GroupProxy, GroupAdmin)