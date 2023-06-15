from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from .views import CatalogViewSet, ProductViewSet, TagList

router_product = DefaultRouter()
router_product.register(r"product", ProductViewSet)

urlpatterns = [
	path("categories", CatalogViewSet.as_view({"get": "get_categories"})),
	path("products/popular", CatalogViewSet.as_view({"get": "get_product_popular"})),
	path("products/limited", CatalogViewSet.as_view({"get": "get_product_limit"})),
	# path("catalog", CatalogList.as_view()),
	# path("catalog/<int:pk>", CatalogList.as_view())
	path("tags", TagList.as_view({"get": "list"})),
	path("", include(router_product.urls)),

	# /products/popular
	# /products/limited
	# /sales
	# /banners:

	# /product/{id}/review:
	# /basket:
	# /orders:
	# /orders/{id}:

]
