"""
URL configuration for market project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from account.views import RegisterView, LoginView, LoginWithTokenView


schema_view = get_schema_view(
    openapi.Info(
        title="Market API",
        default_version='v1',
        description='Market API documentation',
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="ibrohimmaqsudov222@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('stores/', include('stores.urls')),
    path('account/', include('account.urls')),
    path('categories/', include('categories.urls')),
    path('products/', include('products.urls')),
    path('likes/', include('likes.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('cards/', include('card_of_users.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)