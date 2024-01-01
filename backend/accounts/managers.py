'''user manager'''

from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _

# import modules
from accounts.models import *

#  -- user

# doyans user manager
class DoyansUserManager(BaseUserManager):
    '''manage doyans custom user'''

    def create_user(self,email,password,**extra_fields):
        '''crate user with email and username and password'''
        
        # raise error for no email
        if not email:
            raise ValueError(_("provide email"))
        
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        
        return user

    def create_superuser(self,email,password,**extra_fields):
        '''create super user'''
        
        # set fields as true
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        extra_fields.setdefault("is_active",True)
        extra_fields.setdefault("is_level_pro",True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("staff access must be true"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("superuser access must be true"))
        
        return self.create_user(email,password, **extra_fields)



