from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework import viewsets, generics, status
from rest_framework.decorators import action
from rest_framework.response import Response

from app_basket.models import Basket
from app_basket.serializers import BasketSerializer, MySerializer
from app_shop.serializers import ProductPopularLimitedSerializer


# Create your views here.
class BasketViewSet(viewsets.ViewSet):
	queryset = Basket.objects.all()

	def get_object(self):
		basket_user = self.queryset.filter(profile__pk=self.request.user.pk)
		return basket_user

	@action(detail=True, methods=["get"])
	def get_basket(self, request):
		basket_items = self.get_object()
		serializer = BasketSerializer(basket_items, many=True)
		return Response(serializer.data)

	def update_basket(self, request, operation):
		serializer = MySerializer(data=request.data)
		if serializer.is_valid():
			basket_items = self.get_object().filter(products__pk=request.data["id"]).first()
			if basket_items:
				if operation == "add":
					basket_items.count = request.data["count"]
				elif operation == "delete":
					basket_items.delete()
				basket_items.save()
			serializer = BasketSerializer(self.get_object(), many=True)
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	@action(detail=False, methods=["post"])
	def post_basket(self, request):
		return self.update_basket(request, "add")

	@action(detail=True, methods=["delete"])
	def delete_basket(self, request):
		return self.update_basket(request, "delete")
