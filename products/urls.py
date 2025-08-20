from django.urls import path
from .views import ProductListCreateView, ProductDetailView, ProductImageListCreateView, ProductImageDeleteView

urlpatterns = [
    path('', ProductListCreateView.as_view(), name='product-list-create'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('<int:product_id>/images/', ProductImageListCreateView.as_view(), name='product-image-list-create'),
    path('images/<int:pk>/', ProductImageDeleteView.as_view(), name='product-image-delete'),
]