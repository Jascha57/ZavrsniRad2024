from django.contrib import admin
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe

from .models import CustomUser
from django.contrib.auth.models import Group

class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            output.append(f'<a href="{image_url}" target="_blank"><img src="{image_url}" alt="profile picture" width="50" height="50" style="object-fit: cover;"/></a>')
        output.append(super().render(name, value, attrs))
        return mark_safe(''.join(output))

class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser

    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active',)
    search_fields = ('email', 'first_name', 'last_name',)
    exclude = ('password',)

    def has_add_permission(self, request):
        return False
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'profile_picture':
            request = kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super().formfield_for_dbfield(db_field, **kwargs)

class GroupAdmin(admin.ModelAdmin):
    pass

class GroupProxy(Group):
    readonly_fields = ('name',)

    class Meta:
        proxy = True
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)
admin.site.register(GroupProxy, GroupAdmin)