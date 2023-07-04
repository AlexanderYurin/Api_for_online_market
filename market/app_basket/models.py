from django.core.validators import MinValueValidator, MaxValueValidator
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


class Order(models.Model):
    createdAt = models.DateTimeField(auto_created=True, auto_now_add=True)
    city = models.CharField(max_length=128, blank=True)
    address = models.CharField(max_length=255, blank=True)
    deliveryType = models.CharField(max_length=128, blank=True)
    paymentType = models.CharField(max_length=128, blank=True, choices=[("online", "Online")])
    status = models.CharField(max_length=128, blank=True)
    basket = models.ManyToManyField(Basket)


class Payment(models.Model):
    number = models.PositiveIntegerField(validators=[MinValueValidator(1000000000000000),
                                                     MaxValueValidator(9999999999999999)])
    name = models.CharField(max_length=255)
    month = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    year = models.PositiveIntegerField(validators=[MinValueValidator(2023), MaxValueValidator(2030)])
    code = models.PositiveIntegerField(validators=[MinValueValidator(100), MaxValueValidator(999)])

