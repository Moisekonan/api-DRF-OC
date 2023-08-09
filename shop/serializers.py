from rest_framework.serializers import ModelSerializer

from .models import Category, Product, Article

# path: shop/serializers.py
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'active', 'date_created', 'date_updated']

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'date_created', 'date_updated']
        
class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'name', 'price', 'product', 'date_created', 'date_updated']
        
