from django.urls import path

from app_shop.views import CategoryList

urlpatterns = [
    path("categories", CategoryList.as_view()),
    # /catalog
    # /catalog/{id}
    # /products/popular
    # /products/limited
    # /sales
    # /banners:
    # /product/{id}
    # /product/{id}/review:
    # /basket:
    # /orders:
    # /orders/{id}:

]
