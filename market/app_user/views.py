from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework import mixins
from app_user.models import Profile
from app_user.serializers import UserSerializers


class UserApi(mixins.ListModelMixin, viewsets.GenericViewSet):
	queryset = Profile.objects.all()
	serializer_class = UserSerializers
	pagination_class = None


	@action(detail=True, methods=["post"])
	def post_profile(self, request):
		product = self.get_object()
		if request.method == "POST":
			print(1)
			# serializer = ReviewSerializer(data=request.data)
			# if serializer.is_valid():
			# 	review = Review(product=product, **serializer.validated_data)
			# 	review.save()
			# 	serializer = ReviewSerializer(product.reviews, many=True)
			# 	return Response(serializer.data)
			# else:
			# 	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	@action(detail=True, methods=["post"], url_path="password")
	def post_profile_password(self, request):
		pass

	@action(detail=True, methods=["post"], url_path="avatar")
	def post_profile_avatar(self, request):
		pass