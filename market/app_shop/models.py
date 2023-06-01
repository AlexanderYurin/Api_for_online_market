from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Category(models.Model):
    """
    Модель категорий товаров
    """
    title = models.CharField(max_length=255)

    # product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сategory'
        verbose_name_plural = 'Сategories'
        ordering = ('title',)


class Subcategories(models.Model):
    title = models.CharField(max_length=255, default='')
    category = models.ForeignKey("Category", on_delete=models.CASCADE, default='123')

# class Product(models.Model):
#     """
#     Модель описывающая товар,
#     связана с моделью Review(отзыв) отношение один ко многим.
#     """
#     title = models.CharField()
#     photo = models.ImageField()
#     description = models.CharField()
#     price = models.IntegerField()
#     count = models.IntegerField
#     date = models.DateTimeField(auto_created=True)
#     review = models.ForeignKey("Review", on_delete=models.CASCADE)
#     rating = models.FloatField(default=0)
#     href = models.URLField()
#     freeDelivery = models.BooleanField()
#
#
#
#
#     class Meta:
#         verbose_name_plural = _("Products")
#         verbose_name = _("Products")
#         ordering = ("title",)
#
#     def __str__(self):
#         return {self.title}
#
#
# class Review(models.Model):
#     """
#     Модель для отзыва на товар
#     """
#     description = models.CharField()
#     date_of_creation = models.DateField()
#
#     class Meta:
#         verbose_name_plural = _("Reviews")
#         verbose_name = _("Review")
#         ordering = ("date_of_creation",)
