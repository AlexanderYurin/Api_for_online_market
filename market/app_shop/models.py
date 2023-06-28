from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Avg


class Category(models.Model):
	"""
    Модель категорий товаров
    """
	title = models.CharField(max_length=255, verbose_name="Title", unique=True)
	image = models.ForeignKey("Image", on_delete=models.CASCADE, blank=True, related_name="image")

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
	src = models.FileField(upload_to="category", verbose_name="Image", validators=[validate_svg_file])
	alt = models.CharField(max_length=255, verbose_name="Description")

	class Meta:
		verbose_name = "Image"
		verbose_name_plural = "Images"


#
class Product(models.Model):
	"""
    Модель описывающая товар,
    связана с моделью Review(отзыв) отношение один ко многим.
    """
	category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="product")
	title = models.CharField(max_length=100, verbose_name="Title")
	description = models.CharField(max_length=256, verbose_name="Description")
	fullDescription = models.TextField(verbose_name="Full description")
	price = models.IntegerField(default=0, verbose_name="Price")
	count = models.IntegerField(verbose_name="Count", default=0)
	date = models.DateTimeField(auto_created=True)
	freeDelivery = models.BooleanField(default=False, verbose_name="Free Delivery")
	sale = models.FloatField(default=0, verbose_name="Sale")
	available = models.BooleanField(default=True, verbose_name="Available")
	images = models.ManyToManyField("ImagesProduct", default=None)
	tags = models.ManyToManyField("Tag", default=None)

	class Meta:
		verbose_name_plural = "Products"
		verbose_name = "Product"
		ordering = ("title",)

	def __str__(self):
		return self.title


class ImagesProduct(models.Model):
	image_url = models.ImageField()


class Review(models.Model):
	"""
    Модель для отзыва на товар
    """
	product = models.ForeignKey("Product", on_delete=models.CASCADE, verbose_name=Product, related_name="reviews")
	author = models.CharField(verbose_name="Author", max_length=100)
	email = models.EmailField(verbose_name="Email")
	text = models.CharField(verbose_name="Text", max_length=256)
	date = models.DateField(auto_now_add=True)
	rate = models.IntegerField(blank=True)

	class Meta:
		verbose_name_plural = "Reviews"
		verbose_name = "Review"
		ordering = ("-date",)


class Specification(models.Model):
	product = models.ForeignKey("Product",
								on_delete=models.CASCADE,
								verbose_name="Product",
								related_name="specifications")
	name = models.CharField(max_length=256, verbose_name="Name")
	value = models.CharField(max_length=256, verbose_name="Value")


class Tag(models.Model):
	name = models.CharField(max_length=255, verbose_name="Name", unique=True)
	id = models.CharField(max_length=50, primary_key=True)

	def clean(self):
		if self.name.lower() != self.id.lower():
			raise ValidationError("Name and ID must be the same.")

	def __str__(self):
		return self.name
