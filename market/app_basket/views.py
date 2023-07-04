from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework import viewsets, generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from app_basket.models import Basket, Order
from app_basket.serializers import BasketSerializer, PostDeleteBasketSerializer, OrderSerializer
from app_shop.models import Product


# Create your views here.

class BasketViewSet(viewsets.ViewSet):
	queryset = Basket.objects.all()

	def get_object(self):
		if self.request.authenticators:
			basket_user = self.queryset.filter(profile=self.request.user)
			return basket_user

	@action(detail=True, methods=["get"])
	def get_basket(self, request):
		basket_items = self.get_object()
		serializer = BasketSerializer(basket_items, many=True)
		return Response(serializer.data)

	@action(detail=False, methods=["post"])
	def post_basket(self, request):
		serializer = PostDeleteBasketSerializer(data=request.data, instance=self.get_object())

		return Response(status=status.HTTP_201_CREATED)

	@action(detail=True, methods=["delete"])
	def delete_basket(self, request):
		serializer = PostDeleteBasketSerializer(data=request.data)


class OrderViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer
