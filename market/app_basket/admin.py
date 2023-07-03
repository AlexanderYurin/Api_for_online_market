from django.contrib import admin

from app_basket.models import Basket


# Register your models here.
class BasketAdmin(admin.ModelAdmin):
	pass


admin.site.register(Basket, BasketAdmin)
