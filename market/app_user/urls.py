from django.urls import path
from app_user.views import UserApi

urlpatterns = [
	path("profile", UserApi.as_view({"get": "get_profile", "post": "get_profile"})),
	path("profile/password", UserApi.as_view({"post": "profile_password", "get": "profile_password"})),
	path("profile/avatar", UserApi.as_view({"post": "profile_avatar", "get": "profile_avatar"}))
]
