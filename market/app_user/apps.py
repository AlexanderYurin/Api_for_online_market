from django.apps import AppConfig


class AppUserConfig(AppConfig):
	default_auto_field = 'django.db.models.BigAutoField'
	name = 'app_user'
	verbose_name = 'Profile'

	def ready(self):
		import app_user.signals


default_app_config = 'app_user.apps.AppUserConfig'
