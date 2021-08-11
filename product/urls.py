from django.urls import path
from .api import ProductCreateApi, ProductApi, ProductUpdateApi, ProductDeleteApi, CategoryCreateApi, CategoryApi, CategoryUpdateApi, CategoryDeleteApi, SubCategoryApi, SubCategoryCreateApi, SubCategoryUpdateApi, SubCategoryDeleteApi


urlpatterns = [
    path('api',ProductApi.as_view()),
    path('api/create',ProductCreateApi.as_view()),
    path('api/<int:pk>',ProductUpdateApi.as_view()),
    path('api/<int:pk>/delete',ProductDeleteApi.as_view()),
    path('api/category',CategoryApi.as_view()),
    path('api/category/create',CategoryCreateApi.as_view()),
    path('api/category/<int:pk>',CategoryUpdateApi.as_view()),
    path('api/category/<int:pk>/delete',CategoryDeleteApi.as_view()),
    path('api/subcategory',SubCategoryApi.as_view()),
    path('api/subcategory/create',SubCategoryCreateApi.as_view()),
    path('api/subcategory/<int:pk>',SubCategoryUpdateApi.as_view()),
    path('api/subcategory/<int:pk>/delete',SubCategoryDeleteApi.as_view()),
]