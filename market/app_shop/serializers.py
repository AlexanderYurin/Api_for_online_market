from rest_framework import serializers

from app_shop.models import Category, Subcategories


class CategorySerializers(serializers.ModelSerializer):
    """Серилазер для модели Category"""

    class Meta:
        model = Category
        fields = ("title")



