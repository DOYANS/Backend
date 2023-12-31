from rest_framework.serializers import ModelSerializer

# import modules
from accounts.models import *

# create serializers

#  -- users

# doyans user information
class DoyansUserSerialzer(ModelSerializer):

    class Meta:
        model = DoyansUser
        fields = [
            'email,fullname',
            ]