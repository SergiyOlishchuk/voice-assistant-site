from django.contrib import admin

from users.models import User

# Register your models here.
# admin.site.register(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "email"]

    search_fields = ["username", "first_name", "last_name", "email"]

    fields = [
        "username",
        ("first_name", "last_name"),
        "email",
        "token",
        "image",
        ("date_joined", "last_login"),
        ("is_staff", "is_active", "is_superuser"),
        ("groups", "user_permissions"),
    ]

    readonly_fields = [
        "date_joined", "last_login",  "is_superuser", 
    ]
    
    list_filter = ['is_staff', 'is_active']
