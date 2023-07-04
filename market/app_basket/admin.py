from django.contrib import admin

from app_basket.models import Basket, Order


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
	pass



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	pass

