from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UA
from users.models import User

@admin.register(User)
class UserAdmin(UA):
    pass

# Register your models here.
