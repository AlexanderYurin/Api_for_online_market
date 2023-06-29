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


class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = ("name",)


class ReviewSerializer(serializers.ModelSerializer):
	class Meta:
		model = Review
		fields = ['author', 'email', 'text', 'rate', 'date']


class SpecificationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Specification
		fields = ['name', 'value']


class ImagesProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = ImagesProduct
		fields = ('image_url',)


class ProductSerializer(serializers.ModelSerializer):
	images = ImagesProductSerializer(many=True)
	tags = TagSerializer(many=True)
	reviews = ReviewSerializer(many=True)
	specifications = SpecificationSerializer(many=True)
	href = serializers.SerializerMethodField()
	rating = serializers.SerializerMethodField()

	class Meta:
		model = Product
		fields = ['id', 'category', 'price', 'count', 'date', 'title', 'description', 'fullDescription',
				  'href', 'freeDelivery', 'images', 'tags', 'reviews', 'specifications', 'rating']

	def get_href(self, obj):
		return "/product/{id}".format(
			id=obj.pk
		)

	def get_rating(self, obj):
		average_rating = obj.reviews.aggregate(Avg("rate")).get("rate__avg")
		return average_rating

	def to_representation(self, instance):
		representation = super().to_representation(instance)
		representation["tags"] = [tag["name"] for tag in representation['tags']]
		representation["images"] = [str(image["image_url"]) for image in representation["images"]]
		return representation


class ProductPopularLimitedSerializer(ProductSerializer):
	reviews = serializers.SerializerMethodField()

	class Meta:
		model = Product
		fields = ['id', 'category', 'price', 'count', 'date', 'title', 'description',
				  'href', 'freeDelivery', 'images', 'tags', 'reviews', 'rating']

	def get_reviews(self, obj):
		number_reviews = obj.reviews.count()
		return number_reviews


class CatalogSerializer(serializers.ModelSerializer):
	product = ProductSerializer(many=True)

	class Meta:
		model = Category
		fields = ["product"]
