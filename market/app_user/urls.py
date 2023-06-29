from django.urls import path, include
from app_user.views import UserApi
from rest_framework.routers import DefaultRouter

router_profile = DefaultRouter()
router_profile.register(r"profile", UserApi)

urlpatterns = [
	path("", include(router_profile.urls)),
]
