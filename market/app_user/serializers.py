from rest_framework import serializers

from app_user.models import Profile


class UserSerializers(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = (
			"fullName",
			"email",
			"phone",
			"avatar"
		)


class UserPasswordSerializers(UserSerializers):
	password = serializers.SerializerMethodField()

	class Meta:
		model = Profile
		fields = ("password",)

	def get_password(self, obj):
		return obj.password


class UserAvatarSerializers(UserSerializers):
	class Meta:
		model = Profile
		fields = ("avatar",)
