from django.contrib import admin

from users.models import User


class UserAdmin(admin.ModelAdmin):
    # list options
    list_display = ('username', 'email', 'is_superuser', 'created_at', )
    list_filter = ('is_superuser', 'created_at', )

    # detail options
    # fields = ['username',]
    # exclude = ['password', ]
    fieldsets = (
        ('Dados do usuário', {
            'fields': (
                'username', 'password', 'email', ('first_name', 'last_name',), 'picture',
            ),
        }),
        ('Permissões usuário', {
            'fields': (
                'is_superuser', 'is_staff', 'groups', 'user_permissions',
            ),
        }),
        ('Datas', {
            'fields': (
                ('date_joined', 'last_login', ),
            ),
        }),
    )


# Register the admin class with the associated model
admin.site.register(User, UserAdmin)
