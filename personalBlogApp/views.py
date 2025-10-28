from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import *
from .models import *
from .filter import *

# Create your views here.
