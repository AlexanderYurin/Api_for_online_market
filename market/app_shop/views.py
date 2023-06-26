from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins
from app_shop.models import Category, Product, Tag, Review
from app_shop.serializers import (
	CategorySerializer,
	ProductSerializer,
	TagSerializer,
	ReviewSerializer, ProductPopularLimitedSerializer,
)
from django.db.models import Avg


class CatalogViewSet(viewsets.ViewSet):
	@action(detail=True, methods=["get"])
	def get_categories(self, request):
		categories = Category.objects.all()
		serializers = CategorySerializer(categories, many=True)
		return Response(serializers.data)

	@action(detail=True, methods=["get"])
	def get_catalog(self, request):
		queryset = Product.objects.all().order_by("-date")
		paginator = PageNumberPagination()
		page_objects = paginator.paginate_queryset(queryset, request)
		serializer = ProductSerializer(page_objects, many=True)
		response_data = {
			"items": serializer.data,
			"currentPage": paginator.page.number,
			"lastPage": paginator.page.paginator.num_pages,

		}
		return Response(response_data)

	def get_catalog_id(self, request, pk):
		queryset = Product.objects.filter(category=pk).order_by("-date")
		paginator = PageNumberPagination()
		page_objects = paginator.paginate_queryset(queryset, request)
		serializer = ProductSerializer(page_objects, many=True)
		response_data = {
			"items": serializer.data,
			"currentPage": paginator.page.number,
			"lastPage": paginator.page.paginator.num_pages,

		}
		return Response(response_data)

	@action(detail=True, methods=["get"])
	def get_product_popular(self, request):
		queryset = Product.objects.filter(reviews__isnull=False).annotate(
			total_rate=Avg("reviews__rate")
		)
		sorted_product_popular = queryset.order_by("-total_rate")[:5]
		serializers = ProductPopularLimitedSerializer(sorted_product_popular, many=True)
		return Response(serializers.data)

	@action(detail=True, methods=["get"])
	def get_product_limit(self, request):
		product_limit = Product.objects.all().order_by("-count")[:5]
		serializers = ProductPopularLimitedSerializer(product_limit, many=True)
		return Response(serializers.data)

	@action(detail=True, methods=["get"])
	def get_banners(self, request):
		product_limit = Product.objects.all().order_by("-count")[:5]
		serializers = ProductSerializer(product_limit, many=True)
		return Response(serializers.data)


class ProductViewSet(viewsets.GenericViewSet):
	queryset = Product.objects.all()

	def post_product_id_review(self, request, pk=None):
		product = self.get_object()
		if request.method == "POST":
			serializer = ReviewSerializer(data=request.data)
			if serializer.is_valid():
				review = Review(product=product, **serializer.validated_data)
				review.save()
				serializer = ReviewSerializer(product.reviews, many=True)
				return Response(serializer.data)
			else:
				return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	@action(detail=True, methods=["get"])
	def get_product_detail(self, request, pk=None):
		product = self.get_object()
		serializer = ProductSerializer(product)
		return Response(serializer.data)


class TagList(mixins.ListModelMixin, viewsets.GenericViewSet):
	"""
    Класс для получения всех тегов.
    :param queryset содержит все теги.
    :params serializer_class  преобразования объектов модели
    Tag в JSON формат и наоборот.
    """
	queryset = Tag.objects.all()
	serializer_class = TagSerializer
	pagination_class = None
