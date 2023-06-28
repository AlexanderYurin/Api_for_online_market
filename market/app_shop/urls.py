from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CatalogViewSet, ProductViewSet, TagList

router_product = DefaultRouter()
router_product.register(r"product", ProductViewSet)

urlpatterns = [
	path("categories", CatalogViewSet.as_view({"get": "get_categories"})),
	path("products/popular", CatalogViewSet.as_view({"get": "get_product_popular"})),
	path("products/limited", CatalogViewSet.as_view({"get": "get_product_limit"})),
	path("banners", CatalogViewSet.as_view({"get": "get_banners"})),
	path("catalog", CatalogViewSet.as_view({"get": "get_catalog"})),
	path("catalog/<int:pk>", CatalogViewSet.as_view({"get": "get_catalog_id"})),
	path("tags", TagList.as_view({"get": "list"})),
	path("", include(router_product.urls)),
	path("product<int:pk>/review", ProductViewSet.as_view({"post": "post_product_id_review"})),
	path("products/<int:pk>", ProductViewSet.as_view({"get": "get_product_detail"})),


	# /sales
	# /product/{id}/review:
	# /basket:
	# /orders:
	# /orders/{id}:

]
