from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Like
from .serializers import LikeSerializer


class ToggleLikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, product_id):
        like, created = Like.objects.get_or_create(
            user=request.user,
            product_id=product_id
        )
        if not created:
            like.delete()
            return Response({"detail": "Like removed"}, status=status.HTTP_200_OK)

        serializer = LikeSerializer(like)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class MyLikesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        likes = Like.objects.filter(user=request.user)
        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data)