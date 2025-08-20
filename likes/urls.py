from django.urls import path
from .views import ToggleLikeView, MyLikesView

urlpatterns = [
    path('toggle/<int:product_id>/', ToggleLikeView.as_view(), name='toggle-like'),
    path('my/', MyLikesView.as_view(), name='my-likes'),
]
