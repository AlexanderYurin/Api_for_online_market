from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action

from app_shop.models import Category, Product, Tag, Review
from app_shop.serializers import CategorySerializer, ProductSerializer, CatalogSerializer, TagSerializer, \
	ReviewSerializer


class CatalogViewSet(viewsets.ViewSet):

	@action(detail=True, methods=["get"])
	def get_categories(self, request):
		categories = Category.objects.all()
		serializers = CategorySerializer(categories, many=True)
		return Response(serializers.data)

	@action(detail=True, methods=["get"])
	def get_product_popular(self, request):
		product_popular = Product.objects.all()
		serializers = ProductSerializer(product_popular, many=True)
		return Response(serializers.data)

	@action(detail=True, methods=["get"])
	def get_product_limit(self, request):
		product_popular = Product.objects.all().order_by("count")
		serializers = ProductSerializer(product_popular, many=True)
		return Response(serializers.data)


class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	pagination_class = None

	@action(detail=True, methods=["get", "post"], url_path="review")
	def post_product_id_review(self, request, pk=None):
		# Получаем товар по его ID
		product = self.get_object()

		# Если метод запроса - POST, сохраняем отзыв
		if request.method == "POST":
			serializer = ReviewSerializer(data=request.data)
			if serializer.is_valid():
				review = Review(product=product, **serializer.validated_data)
				review.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			else:
				return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		# Если метод запроса - GET, возвращаем все отзывы для товара
		elif request.method == 'GET':
			reviews = product.review.all()
			serializer = ReviewSerializer(reviews, many=True)
			return Response(serializer.data)


# class CatalogList(APIView):
#     # "name": "string",
#     # "minPrice": 0,
#     # "maxPrice": 0,
#     # "freeDelivery": false,
#     # "available": true
#     def get(self, request, format=None):
#         queryset = Product.objects.all()
#         page = request.GET.get('page')
#         category = request.GET.get('category')
#         sort = request.GET.get('sort')
#         sort_type = request.GET.get('sortType')
#         name = request.GET.get('filter[name]')
#         min_price = request.GET.get('filter[minPrice]')
#         max_price = request.GET.get('filter[maxPrice]')
#         free_delivery = request.GET.get('filter[freeDelivery]')
#         available = request.GET.get('filter[available]')
#         limit = request.GET.get('limit')
#
#         if category != '0':
#             queryset = queryset.filter(category=category)
#
#         # if name:
#         #     queryset = queryset.filter(name__icontains=name)
#
#         if min_price and max_price:
#             queryset = queryset.filter(price__range=(min_price, max_price))
#
#         if free_delivery == 'true':
#             queryset = queryset.filter(free_delivery=True)
#
#         # if available == 'true':
#         #     queryset = queryset.filter(available=True)
#
#         if sort and sort_type:
#             if sort_type == 'inc':
#                 queryset = queryset.order_by(sort)
#             elif sort_type == 'dec':
#                 queryset = queryset.order_by(f'-{sort}')
#
#         if limit:
#             queryset = queryset[:int(limit)]
#
#         data = list(queryset.values())
#         categories = Category.objects.all()
#         serializer = CatalogSerializer(categories, many=True)
#         return Response(serializer.data)

class TagList(viewsets.ReadOnlyModelViewSet):
	"""
    Класс для получения всех тегов.
    :param queryset содержит все теги.
    :params serializer_class  преобразования объектов модели
    Tag в JSON формат и наоборот.
    """
	queryset = Tag.objects.all()
	serializer_class = TagSerializer
	pagination_class = None
