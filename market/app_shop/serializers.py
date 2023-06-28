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
		fields = ["id", "name"]


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
	images = serializers.SerializerMethodField()
	tags = serializers.SerializerMethodField()
	reviews = ReviewSerializer(many=True)
	specifications = SpecificationSerializer(many=True)
	href = serializers.SerializerMethodField()
	rating = serializers.SerializerMethodField()

	class Meta:
		model = Product
		fields = ['id', 'category', 'price', 'count', 'date', 'title', 'description', 'fullDescription',
				  'href', 'freeDelivery', 'images', 'tags', 'reviews', 'specifications', 'rating']

	def get_tags(self, obj):
		return [tag.name for tag in obj.tags.all()]

	# def get_images(self, obj):
	# 	return ImagesProductSerializer(obj.images.all(), many=True).data

	def get_href(self, obj):
		return "/product/{id}".format(
			id=obj.pk
		)

	def get_rating(self, obj):
		average_rating = obj.reviews.aggregate(Avg("rate")).get("rate__avg")
		return average_rating


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
