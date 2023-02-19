from rest_framework import serializers
from ..models import Room, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'parent', 'title', 'slug', 'photo', 'description')


class CategoryWithSubcategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'parent', 'title', 'slug', 'photo', 'description', 'subcategories')

    subcategories = serializers.SerializerMethodField('get_subcategories')

    def get_subcategories(self, instance):
        return CategorySerializer(instance.childrens.all(), many=True, context=self.context).data



class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'title', 'slug', 'categories')

    categories = serializers.SerializerMethodField('get_categories')

    def get_categories(self, instance):
        root_categories = instance.categories.filter(parent=None)
        return CategoryWithSubcategoriesSerializer(root_categories, many=True, context=self.context).data
