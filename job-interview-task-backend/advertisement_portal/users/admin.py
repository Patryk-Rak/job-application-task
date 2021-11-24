from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdmin(UserAdmin):
    ordering = ('email',)
    list_display = ('email', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name', 'last_login')
    readonly_fields = ('id', 'date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'date_joined', 'last_login')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_admin', 'is_superuser')}),
        )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name',
                       'is_active', 'is_staff', 'is_admin', 'is_superuser'),
        }),

    )


admin.site.register(Account, AccountAdmin)

