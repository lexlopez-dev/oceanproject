from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from .models import Organization
from .models import Account
from .serializers import UserSerializer
from .serializers import OrganizationSerializer
from .serializers import AccountSerializer

# Create your views here.

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class OrganizationView(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class AccountView(viewsets.ModelViewSet):
    queryset = Account.objects.all();
    serializer_class = AccountSerializer