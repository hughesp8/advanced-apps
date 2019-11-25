from django.shortcuts import render
from rest_framework import viewsets

from .serializers import LuasStopSerializer
from .models import LuasStop

class LuasStopViewSet(viewsets.ModelViewSet):
    queryset = LuasStop.objects.all().order_by('short_name')
    serializer_class = LuasStopSerializer

# Create your views here.
