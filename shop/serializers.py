from rest_framework import serializers

from shop.models import Category, Product, Article

# Partie ArticleSerializer
class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['id', 'date_created', 'date_updated', 'name', 'price', 'product']

# Partie ProductListSerializer et ProductDetailSerializer
class ProductListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['id', 'date_created', 'date_updated', 'name', 'category']

class ProductDetailSerializer(serializers.ModelSerializer):

    articles = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'date_created', 'date_updated', 'name', 'category', 'articles']

    def get_articles(self, instance):
        queryset = instance.articles.filter(active=True)
        serializer = ArticleSerializer(queryset, many=True)
        return serializer.data

# Partie CategoryListSerializer et CategoryDetailSerializer
class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'date_created', 'date_updated', 'name']


class CategoryDetailSerializer(serializers.ModelSerializer):

    products = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'date_created', 'date_updated', 'name', 'products']

    def get_products(self, instance):
        queryset = instance.products.filter(active=True)
        serializer = ProductDetailSerializer(queryset, many=True)
        return serializer.data