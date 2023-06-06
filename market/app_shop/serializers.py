from rest_framework import serializers

from app_shop.models import Category, Subcategories, Image





class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('src', 'alt')


class SubcategoriesSerializer(serializers.ModelSerializer):
    image = ImageSerializer()
    href = serializers.SerializerMethodField()

    class Meta:
        model = Subcategories
        fields = ('id', 'title', 'image', 'href' )

    def get_href(self, obj):
        return "/catalog/{id}".format(
            id=obj.pk
        )



class CategorySerializer(serializers.ModelSerializer):
    image = ImageSerializer()
    subcategories = SubcategoriesSerializer(many=True)
    href = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'title', 'image', 'href', 'subcategories')

    def get_href(self, obj):
        return "/catalog/{id}".format(
            id=obj.pk
        )
