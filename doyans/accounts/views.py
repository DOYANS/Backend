from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication,BasicAuthentication

from rest_framework_simplejwt.tokens import RefreshToken,OutstandingToken,BlacklistedToken

# import modules
from accounts.models import *
from accounts.serializers import *
from accounts.permissions import *
from accounts.authentications import *

# Create your views here.
