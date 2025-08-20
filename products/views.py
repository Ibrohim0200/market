from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Product, ProductImage
from .serializer import ProductSerializer, ProductImageSerializer
from stores.models import Store


class ProductListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        store = Store.objects.filter(owner=request.user).first()
        if not store:
            return Response({"detail": "Sizning do‘koningiz yo‘q."}, status=status.HTTP_404_NOT_FOUND)

        products = Product.objects.filter(store=store)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        try:
            store = Store.objects.get(owner=request.user)
            product = Product.objects.get(pk=pk, store=store)
        except (Store.DoesNotExist, Product.DoesNotExist):
            return Response({"detail": "Mahsulot topilmadi yoki sizga tegishli emas."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            store = Store.objects.get(owner=request.user)
            product = Product.objects.get(pk=pk, store=store)
        except (Store.DoesNotExist, Product.DoesNotExist):
            return Response({"detail": "Mahsulot topilmadi yoki sizga tegishli emas."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            store = Store.objects.get(owner=request.user)
            product = Product.objects.get(pk=pk, store=store)
        except (Store.DoesNotExist, Product.DoesNotExist):
            return Response({"detail": "Mahsulot topilmadi yoki sizga tegishli emas."}, status=status.HTTP_404_NOT_FOUND)

        product.delete()
        return Response({"detail": "Mahsulot o‘chirildi."}, status=status.HTTP_204_NO_CONTENT)


class ProductImageListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, product_id):
        try:
            store = Store.objects.get(owner=request.user)
            product = Product.objects.get(pk=product_id, store=store)
        except (Store.DoesNotExist, Product.DoesNotExist):
            return Response({"detail": "Mahsulot topilmadi yoki sizga tegishli emas."}, status=status.HTTP_404_NOT_FOUND)

        images = ProductImage.objects.filter(product=product)
        serializer = ProductImageSerializer(images, many=True)
        return Response(serializer.data)

    def post(self, request, product_id):
        try:
            store = Store.objects.get(owner=request.user)
            product = Product.objects.get(pk=product_id, store=store)
        except (Store.DoesNotExist, Product.DoesNotExist):
            return Response({"detail": "Mahsulot topilmadi yoki sizga tegishli emas."}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()
        data['product'] = product.id
        serializer = ProductImageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductImageDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        image = ProductImage.objects.filter(pk=pk, product__store__owner=request.user).first()

        if not image:
            return Response({"detail": "Rasm topilmadi yoki sizga tegishli emas."}, status=status.HTTP_404_NOT_FOUND)
        image.delete()
        return Response({"detail": "Rasm o‘chirildi."}, status=status.HTTP_204_NO_CONTENT)
