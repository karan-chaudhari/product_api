from rest_framework import generics
from rest_framework.response import Response
from .serializer import ProductSerializer, CategorySerializer, SubCategorySerializer
from .models import Product, Category, SubCategory

class SubCategoryCreateApi(generics.CreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class SubCategoryApi(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class SubCategoryUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class SubCategoryDeleteApi(generics.DestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class CategoryCreateApi(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryApi(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDeleteApi(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductCreateApi(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductApi(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDeleteApi(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
