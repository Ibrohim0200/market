from django.urls import path
from .views import OrderListCreateView, OrderDeleteView

urlpatterns = [
    path('', OrderListCreateView.as_view(), name='order-list-create'),
    path('<int:pk>/', OrderDeleteView.as_view(), name='order-delete'),
]
