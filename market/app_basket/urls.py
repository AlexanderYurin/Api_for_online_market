from django.urls import path, include

from app_basket.views import BasketViewSet

urlpatterns = [
	path("basket", BasketViewSet.as_view(
		{"get": "get_basket",
		 "post": "post_basket",
		 "delete": "delete_basket"}
	))

]
