from django.urls import  path

#/categories
#/catalog
#/catalog/{id}
#/products/popular
#/products/limited
#/sales
#/banners:
#/product/{id}
#/product/{id}/review:
#/basket:
#/orders:
#/orders/{id}:
from django.urls import path
from rest_framework import permissions

from app_shop.views import CategoryAPI

# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
#

#
# schema_view = get_schema_view(
#    openapi.Info(
#       title="Book API",
#       default_version='v1',
#       description="Test description",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="contact@snippets.local"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=[permissions.AllowAny],
# )

urlpatterns = [
    path('api/categories', CategoryAPI.as_view()),


]