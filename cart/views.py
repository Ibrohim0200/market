from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Cart
from .serializers import CartSerializer

class CartListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        carts = Cart.objects.filter(user=request.user)
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CartSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self, pk, user):
        try:
            return Cart.objects.get(pk=pk, user=user)
        except Cart.DoesNotExist:
            return None

    def get(self, request, pk):
        cart_item = self.get_object(pk, request.user)
        if not cart_item:
            return Response({"detail": "Topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CartSerializer(cart_item)
        return Response(serializer.data)

    def patch(self, request, pk):
        cart_item = self.get_object(pk, request.user)
        if not cart_item:
            return Response({"detail": "Topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CartSerializer(cart_item, data=request.data, partial=True, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cart_item = self.get_object(pk, request.user)
        if not cart_item:
            return Response({"detail": "Topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        cart_item.delete()
        return Response({"detail": "O‘chirildi"}, status=status.HTTP_204_NO_CONTENT)
