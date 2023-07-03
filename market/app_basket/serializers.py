from rest_framework import serializers

from app_basket.models import Basket
from app_shop.models import Product
from app_shop.serializers import ProductPopularLimitedSerializer


class BasketSerializer(serializers.Serializer):
	products = ProductPopularLimitedSerializer()

	class Meta:
		model = Product
		fields = ["__all__"]

	def to_representation(self, instance):
		representation = super().to_representation(instance)
		representation.get("products")["count"] = instance.count
		return representation.get("products")


class MySerializer(serializers.Serializer):
	id = serializers.IntegerField()
	count = serializers.IntegerField()
