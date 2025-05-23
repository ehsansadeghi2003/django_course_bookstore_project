from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm,CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model =CustomUser
    add_form =CustomUserCreationForm
    form =CustomUserChangeForm
    fieldsets=UserAdmin.fieldsets
    add_fieldsets =UserAdmin.fieldsets
admin.site.register(CustomUser,CustomUserAdmin)





