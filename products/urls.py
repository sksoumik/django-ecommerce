from django.contrib import admin
from django.urls import path, re_path
from . import views


urlpatterns = [
    path('products/', views.ProductListView.as_view(), name = 'list_view'),
    path('products-fbv/', views.product_list_view, name='product_list_view'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name = 'detail_view'),
    path('products-fbv/<int:pk>/', views.product_detail_view, name = 'product_detail_view'),
    path('featured/<int:pk>/', views.ProductFeaturedDetailView.as_view(), name = 'product_featured_detail_view'),
    path('featured/', views.ProductFeaturedListView.as_view(), name = 'product_featured_detail_view'),

]


