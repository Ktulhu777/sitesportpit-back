from rest_framework import serializers
from .models import Product, CategoryProduct, Review


class ProductSerializer(serializers.ModelSerializer):
    cat = serializers.CharField()

    class Meta:
        model = Product
        fields = ('id', 'title', 'content', 'photo', 'price', 'time_create', 'cat', 'avg_rating',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProduct
        fields = ('cat_name',)


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.CharField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Review
        fields = ("id", "user", "review", "create_date", "changes", "rating")

    def create(self, validated_data):
        return Review.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.review = validated_data.get("review", instance.review)
        instance.changes = True
        instance.save()
        return instance
