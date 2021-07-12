from django.shortcuts import render
from .serializers import ContactSerializer
from rest_framework.permissions import AllowAny
# from rest_framework.decorators import list_route
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from .models import Contact


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer