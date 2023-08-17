from rest_framework import serializers

from shop.models import Category, Product, Article

# Partie ArticleSerializer
class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['id', 'date_created', 'date_updated', 'name', 'price', 'product']
        
    def validate_price(self, value):
        if value <= 1:
            raise serializers.ValidationError("Le prix doit être supérieu à 1€")
        return value
    
    def validate_product(self, value):
        if value.active is False:
            raise serializers.ValidationError('Le produit est inactif')
        return value


class ArticleDetailSerializer(serializers.ModelSerializer):

    articles = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['id', 'date_created', 'date_updated', 'name', 'price', 'product']

    def get_articles(self, instance):
        queryset = instance.articles.filter(active=True)
        serializer = ArticleListSerializer(queryset, many=True)
        return serializer.data
    
    
# Partie ProductListSerializer et ProductDetailSerializer
class ProductListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['id', 'date_created', 'date_updated', 'name', 'category', 'ecoscore']

class ProductDetailSerializer(serializers.ModelSerializer):

    articles = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'date_created', 'date_updated', 'name', 'category', 'articles']

    def get_articles(self, instance):
        queryset = instance.articles.filter(active=True)
        serializer = ArticleListSerializer(queryset, many=True)
        return serializer.data

# Partie CategoryListSerializer et CategoryDetailSerializer
class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'date_created', 'date_updated', 'name', 'description']

    def validate_name(self, value):
        if Category.objects.filter(name=value).exists():  # Nous vérifions que la catégorie existe
            raise serializers.ValidationError('La catégorie existe déjà') # En cas d'erreur, DRF nous met à disposition l'exception ValidationError
        return value
    
    def validate(self, data):
        if data['name'] not in data['description']:  # Effectuons le contrôle sur la présence du nom dans la description
            raise serializers.ValidationError('Le nom doit figurer dans la description') # En cas d'erreur, DRF nous met à disposition l'exception ValidationError
        return data
class CategoryDetailSerializer(serializers.ModelSerializer):

    products = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'date_created', 'date_updated', 'name', 'products']

    def get_products(self, instance):
        queryset = instance.products.filter(active=True)
        serializer = ProductDetailSerializer(queryset, many=True)
        return serializer.data