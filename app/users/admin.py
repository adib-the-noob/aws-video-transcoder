from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# Register your models here.

User = get_user_model()

class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email','full_name')
    list_filter = ('email', 'is_active',)
    ordering = ('id',)
    list_display = ('__str__', 'email', 'verified', 'is_active')
    fieldsets = (
        (None, {'fields': (
            'full_name',
            'email',
            'profile_picture',
            'password',
            )}),
        ('Permissions',
         {
             'fields': (
                'is_staff',
                'is_superuser',
                'verified',
                'groups',
                'user_permissions'
             )
         }),
    )

    # fieldsets to add a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'full_name',
                'email',
                'profile_picture',
                'password1',
                'is_active',
                'password2',
                'is_staff',
                'groups',
                'user_permissions'
                )}
         ),
    )


admin.site.register(User, UserAdminConfig)

from .models import Otp
admin.site.register(Otp)