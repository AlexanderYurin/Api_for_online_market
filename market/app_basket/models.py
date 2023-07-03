from django.db import models
from django.core.exceptions import ValidationError
from app_shop.models import Product
from app_user.models import Profile


# Create your models here.
def validate_min_quantity(value) -> None:
	if not value > 0:
		raise ValidationError("File format is not supported.")


class Basket(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)
	products = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
	count = models.IntegerField(verbose_name="Quantity", validators=[validate_min_quantity], default=0)

