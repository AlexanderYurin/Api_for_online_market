from django.db import models
from django.core.exceptions import ValidationError


class Category(models.Model):
    """
    Модель категорий товаров
    """
    title = models.CharField(max_length=255, verbose_name="Title", unique=True)
    image = models.ForeignKey("Image", on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ['title']
        verbose_name = "Сategory"
        verbose_name_plural = "Сategories"
        ordering = ("title",)


class Subcategories(models.Model):
    """
     Модель подкатегорий товаров.
    """
    title = models.CharField(max_length=255, verbose_name="Title", unique=True)
    image = models.ForeignKey("Image", on_delete=models.CASCADE, blank=True)
    categories = models.ForeignKey("Category",
                                   on_delete=models.CASCADE,
                                   default=None, null=True,
                                   related_name="subcategories")

    class Meta:
        verbose_name = "Subcategory"
        verbose_name_plural = "Subcategories"
        ordering = ("title",)


def validate_svg_file(value) -> None:
    """
    Функция-валидатор для проверки файла в формате SVG.
    :param value: объект типа UploadedFile, представляющий загруженный файл.
    :raise возникает, если файл имеет расширение, отличное от .svg или не начинается с "<?xml".
    :return: None
    """
    if not value.name.endswith(".svg"):
        raise ValidationError("File format is not supported.")
    content = value.read().decode("utf-8")
    if not content.startswith("<?xml"):
        raise ValidationError("File should start with '<?xml'.")


class Image(models.Model):
    """
    Модель изображений.
    """
    src = models.FileField(verbose_name="Image", validators=[validate_svg_file])
    alt = models.CharField(max_length=255, verbose_name="Description")

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

# class Product(models.Model):
#     """
#     Модель описывающая товар,
#     связана с моделью Review(отзыв) отношение один ко многим.
#     """
#     title = models.CharField(max_length=256, verbose_name="Title")
#     image = models.ImageField(verbose_name="Image", upload_to="product")
#     description = models.CharField(max_length=1000, verbose_name="Description")
#     price = models.IntegerField(default=0, verbose_name="Price")
#     count = models.IntegerField(verbose_name="Count", default=0)
#     date = models.DateTimeField(auto_created=True)
#     review = models.ForeignKey("Review", on_delete=models.CASCADE, null=True, default=None)
#     rating = models.FloatField(default=0, verbose_name="Rating")
#     freeDelivery = models.BooleanField(default=False, verbose_name='Free Delivery')
#     sale = models.FloatField(default=0, verbose_name="Sale")
#
#     #
#
#     class Meta:
#         verbose_name_plural = "Products"
#         verbose_name = "Products"
#         ordering = ("title",)
#
#     def __str__(self):
#         return {self.id}, {self.title}, {self.count}
#
#
# class Review(models.Model):
#     """
#     Модель для отзыва на товар
#     """
#     author = models.CharField("Author")
#     email = models.EmailField(verbose_name="Email")
#     text = models.CharField(verbose_name="Text")
#     date = models.DateField(auto_now_add=True)
#     rate = models.IntegerField(blank=True)
#
#     class Meta:
#         verbose_name_plural = "Reviews"
#         verbose_name = "Review"
#         ordering = ("-date",)
