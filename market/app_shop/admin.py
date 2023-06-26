from django.contrib import admin

from app_shop.models import Category, Subcategories, Image, ImagesProduct, Specification, Tag, Product, Review


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


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)


class ReviewAdmin(admin.ModelAdmin):
    pass


admin.site.register(Review, ReviewAdmin)


class SpecificationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Specification, SpecificationAdmin)


class ImageProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(ImagesProduct, ImageProductAdmin)


class TagAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tag, TagAdmin)
