from django.shortcuts import render
from rest_framework.generics import ListAPIView

from app_shop.models import Category, Subcategories
from app_shop.serializers import CategorySerializers


# Create your views here.

class CategoryAPI(ListAPIView):
    """Представление для получение API модели Book"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

