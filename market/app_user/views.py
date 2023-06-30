from rest_framework import viewsets, status
from rest_framework.decorators import action
from app_user.models import Profile
from app_user.serializers import UserSerializers, UserPasswordSerializers, UserAvatarSerializers
from rest_framework.response import Response


class UserApi(viewsets.ViewSet):
	"""
	ViewSet для работы с профилем пользователя.
	"""

	queryset = Profile.objects.all()
	pagination_class = None

	@action(detail=True, methods=["get", "post"])
	def get_profile(self, request):
		"""
		Получает профиль пользователя.

		GET:
		Возвращает сериализованные данные профиля пользователя.

		POST:
		Обновляет данные пользователя и возвращает сериализованные данные профиля,
		если данные валидны. В противном случае возвращает ошибки сериализации.
		"""
		profile = self.queryset.get(pk=request.user.pk)
		if request.method == "GET":
			serializer = UserSerializers(profile)
			return Response(serializer.data)
		elif request.method == "POST":
			serializer = UserPasswordSerializers(profile, data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			else:
				return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	@action(detail=True, methods=["get", "post"])
	def profile_password(self, request):
		"""
		Получает или обновляет пароль пользователя.

		GET:
		Возвращает сериализованные данные пароля пользователя.

		POST:
		Обновляет пароль пользователя и возвращает сериализованные данные пароля,
		если данные валидны. В противном случае возвращает ошибки сериализации.
		"""
		instance = self.queryset.get(pk=request.user.pk)
		if request.method == "GET":
			serializer = UserPasswordSerializers(instance)
			return Response(serializer.data)
		elif request.method == "POST":
			serializer = UserPasswordSerializers(instance, data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			else:
				return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	@action(detail=True, methods=["get", "post"])
	def profile_avatar(self, request):
		"""
		Получает или обновляет аватар пользователя.

		GET:
		Возвращает сериализованные данные аватара пользователя.

		POST:
		Обновляет аватар пользователя и возвращает сериализованные данные аватара,
		если данные валидны. В противном случае возвращает ошибки сериализации.
		"""
		instance = self.queryset.get(pk=request.user.pk)
		if request.method == "GET":
			serializer = UserAvatarSerializers(instance)
			return Response(serializer.data)
		elif request.method == "POST":
			serializer = UserAvatarSerializers(instance, data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			else:
				return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)