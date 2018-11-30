from django.contrib import admin
from django.urls import path, re_path
from . import views


urlpatterns = [
    path('products/', views.ProductListView.as_view(), name = 'list_view'),
    path('products-fbv/', views.product_list_view, name='product_list_view'),
    # re_path('products/(?P<pk>\d+)/', views.ProductDetailView.as_view(), name = 'detail_view'),
    # re_path('products-fbv/(?P<pk>\d+)/', views.product_detail_view, name = 'product_detail_view'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name = 'detail_view'),
    path('products-fbv/<int:pk>/', views.product_detail_view, name = 'product_detail_view'),

]


