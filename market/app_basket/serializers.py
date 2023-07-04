from rest_framework import serializers

from app_basket.models import Basket, Order
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


class PostDeleteBasketSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    count = serializers.IntegerField()

    def create(self, validated_data: dict):
        return Basket.objects.create(product_id=validated_data.get('id'),
                                     count=validated_data.get('count'))

    def update(self, instance, validated_data: dict):
        old_count = instance.count
        if validated_data['request'].method == 'DELETE':
            instance.count = old_count - validated_data.get("count")
        else:
            instance.count = validated_data.get("count") + old_count
        instance.save()
        return instance

    @staticmethod
    def delete(instance):
        return instance.delete()


class OrderSerializer(serializers.ModelSerializer):
    orderId = serializers.SerializerMethodField()
    fullName = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    phone = serializers.SerializerMethodField()
    createdAt = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    products = BasketSerializer()


    class Meta:
        model = Order
        fields = [
            'orderId', 'createdAt', 'fullName', 'email',
            'phone', 'deliveryType', 'paymentType', 'totalCost',
            'status', 'city', 'address', 'products'
        ]

    @staticmethod
    def get_orderId(obj) -> str:
        return str(obj.id)

    @staticmethod
    def get_fullName(obj) -> str:

        return obj.profile.fullName

    @staticmethod
    def get_email(obj) -> str:
        return obj.profile.email

    @staticmethod
    def get_phone(obj) -> str:
        return obj.profile.phone

    @staticmethod
    def get_deliveryType(obj) -> str:
        for basket in obj.basket.all():
            if not basket.product.freeDelivery:
                return 'paid'
        return 'free'



