# from django.shortcuts import render
# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from drf.serializers import UserSerializer, GroupSerializer #BranchSerializer
#from bank.models import Branch

# class BranchViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows branches to be viewed or edited.
#     """
#     queryset = Branch.objects.all()
#     serializer_class = BranchSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be views or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer