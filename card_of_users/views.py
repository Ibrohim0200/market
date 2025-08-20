from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import CardOfUsers
from .serializers import CardOfUsersSerializer

class CardListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        cards = CardOfUsers.objects.filter(user=request.user)
        serializer = CardOfUsersSerializer(cards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CardOfUsersSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CardDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        try:
            card = CardOfUsers.objects.get(pk=pk, user=request.user)
        except CardOfUsers.DoesNotExist:
            return Response({"detail": "Karta topilmadi yoki sizga tegishli emas."},
                            status=status.HTTP_404_NOT_FOUND)
        card.delete()
        return Response({"detail": "Karta o‘chirildi."}, status=status.HTTP_204_NO_CONTENT)
