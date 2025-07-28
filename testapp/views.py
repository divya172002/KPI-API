from django.shortcuts import render
from rest_framework import viewsets
from .models import FormData
from .serializers import FormDataSerializer
# Create your views here.
class FormDataViewSet(viewsets.ModelViewSet):
    queryset = FormData.objects.all()
    serializer_class = FormDataSerializer



