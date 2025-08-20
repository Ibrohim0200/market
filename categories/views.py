from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Category
from .serializer import CategorySerializer
from stores.models import Store

# Create your views here.

class CategoryListCreateView(ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        store = Store.objects.filter(owner=self.request.user).first()
        return Category.objects.filter(store=store)

    def perform_create(self, serializer):
        store = Store.objects.filter(owner=self.request.user).first()
        serializer.save(store=store)

class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    permission_classes = IsAuthenticated

    def get_queryset(self):
        store = Store.objects.filter(owner=self.request.user).first()
        return Category.objects.filter(store=store)