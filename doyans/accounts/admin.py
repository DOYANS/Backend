from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# import modules
from accounts.models import *
from accounts.forms import *

# create admins

# --user
class DoyansUserAdmin(UserAdmin):

    add_form = DoyansUserCreationForm
    form = DoyansUserChangeForm

    model = DoyansUser

    list_display =[
        'email','username','fullname',
        'is_level_pro',
    ]

    list_filter = [
        'is_level1','is_level2',
    ]

    fieldsets = (
        (None, {"fields":['email','password','username',]}),
        ('Personal',{"fields":["fullname",]}),
        ('Permissions',{
            "fields":[
                "is_staff","is_active",
                "is_level1","is_level2","is_level_pro",
                ]
        }),
    )

    add_fieldsets = (
        (None, {
            "classes": ["wide", ],
            "fields": (
                "email","username","fullname",
                "password1","password",
                "is_level_basic","is_level1","is_level2","is_level_pro",
                "is_staff","is_active","user_permissions",
            )
        }),
    )
    
    search_fields = ['email',]

    ordering =['email',]


# Un-Register your models here
# admin.site.unregister(Groups)

# Register your models here.
admin.site.register(DoyansUser,DoyansUserAdmin)