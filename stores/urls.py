from django.urls import path
from .views import StoreListCreateView, StoreRetrieveUpdateDestroyView

urlpatterns = [
    path('', StoreListCreateView.as_view(), name='store-list-create'),
    path('<int:pk>/', StoreRetrieveUpdateDestroyView.as_view(), name='store-detail'),
]