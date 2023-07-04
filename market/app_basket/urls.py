from django.urls import path, include

from app_basket.views import BasketViewSet, OrderViewSet

urlpatterns = [
	path("basket", BasketViewSet.as_view({"get": "get_basket",
										  "post": "post_basket",
										  "delete": "delete_basket"}
										 )),

	path('orders/', OrderViewSet.as_view({'get': 'list'})),
	# path('orders', OrderView.as_view()),
	# path('orders/<int:pk>', OrderDetailView.as_view()),
	# path('orders/active/'

]
