from rest_framework.views import APIView
from rest_framework.response import Response

from app_shop.models import Category
from app_shop.serializers import CategorySerializer



class CategoryList(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
