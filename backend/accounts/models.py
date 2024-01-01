from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import EmailValidator

# import modules
from accounts.managers import *

# Create your models here.
class DoyansUser(AbstractUser):
    '''custom user'''

    # primary key
    id = models.BigAutoField(primary_key=True)

    # username
    username = models.CharField(
        max_length=50, unique=True, 
        verbose_name="username",
        validators=[UnicodeUsernameValidator()],
    )

    # user email
    email = models.EmailField(
        max_length=50,unique=True, 
        validators=[EmailValidator()],
        verbose_name="user email",
    )

    # user name
    fullname = models.CharField(
        max_length=50,
        verbose_name="full name",
        null=True,blank=True,
    )

    # rights
    is_level_basic = models.BooleanField(
        default=True,
        verbose_name="basic permissions",
    )
    is_level1 = models.BooleanField(
        default=False,
        verbose_name="level-1 permission"
        )
    is_level2 = models.BooleanField(
        default=False,
        verbose_name="level-2 permissions"
    )
    is_level_pro = models.BooleanField(
        default=False,
        verbose_name="all permissions",
    )
    # manager
    objects = DoyansUserManager()

    # key fields
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    REQUIRED_FIELDS = ['email',]


    def __str__(self):
        return self.fullname

    def save(self,*args, **kwargs):

        # if is_level_pro is set as true, all permisisons given
        if self.is_level_pro:
            self.is_level1=True
            self.is_level2=True

        # if full name not given, use username
        if not self.fullname:
            self.fullname = self.username

        super().save(*args, **kwargs)

    def has_perm(self,perm,obj=None):
        '''specific permissions'''
        return True

    def has_module_perms(self,app_label):
        '''view app labels'''
        return True

    @property
    def is_highest(self):
        '''highest permissions'''
        return self.is_level_pro

    @property
    def is_lowest(self):
        '''no permissions -- level1 is false -- return true'''
        return not self.is_level1

    @property
    def _username(self):
        '''username'''
        return self.username
    
    




