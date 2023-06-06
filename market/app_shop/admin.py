from django.contrib import admin

from app_shop.models import Category, Subcategories, Image


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_filter = ("title",)
    list_display = ("id", "title",)


admin.site.register(Category, CategoryAdmin)


class SubcategoriesAdmin(admin.ModelAdmin):
    list_filter = ("title",)
    list_display = ("id", "title",)


admin.site.register(Subcategories, SubcategoriesAdmin)

class ImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Image, ImageAdmin)