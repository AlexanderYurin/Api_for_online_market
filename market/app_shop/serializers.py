from rest_framework import serializers

from app_shop.models import *


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('src', 'alt')


class SubcategoriesSerializer(serializers.ModelSerializer):
    image = ImageSerializer()
    href = serializers.SerializerMethodField()

    class Meta:
        model = Subcategories
        fields = ('id', 'title', 'image', 'href')

    def get_href(self, obj):
        return "/catalog/{id}".format(
            id=obj.pk
        )


class CategorySerializer(serializers.ModelSerializer):
    image = ImageSerializer()
    subcategories = SubcategoriesSerializer(many=True)
    href = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'title', 'image', 'href', 'subcategories')

    def get_href(self, obj):
        return "/catalog/{id}".format(
            id=obj.pk
        )


class ImageProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageProduct
        fields = ['url']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['author', 'email', 'text', 'rate', 'date']


class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = ['name', 'value']


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.StringRelatedField(many=True)
    tag = serializers.StringRelatedField(many=True)
    review = ReviewSerializer(many=True)
    specifications = SpecificationSerializer(many=True)
    href = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'category', 'price', 'count', 'date', 'title', 'description', 'fullDescription',
                  'href', 'freeDelivery', 'image', 'tag', 'review', 'specifications', 'rating']

    def get_href(self, obj):
        return "/catalog/{id}".format(
            id=obj.category.pk
        )

    def get_rating(self, obj):
        average_rating = obj.review.aggregate(Avg("rate")).get("rate__avg")
        return average_rating


class CatalogSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True)
    class Meta:
        model = Category
        fields = ["product"]



