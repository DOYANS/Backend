from django.contrib.auth.forms import UserCreationForm,UserChangeForm

# import modules
from accounts.models import *

# create forms

# -- user

# doyans user creation
class DoyansUserCreationForm(UserCreationForm):

    class Meta:
        model = DoyansUser
        fields = ["email",]

# doyans user change
class DoyansUserChangeForm(UserChangeForm):

    class Meta:
        model = DoyansUser
        fields = ['email','password',]