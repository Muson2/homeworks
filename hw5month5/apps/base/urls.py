from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorAPI, BookAPI, BookListAPI, RegisterAPI
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'authors', AuthorAPI, basename='authors')
router.register(r'books', BookAPI, basename='books')
router.register(r'book-list', BookListAPI, basename='book-list')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterAPI.as_view(), name='register'),
]

urlpatterns += [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # вход
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # обновление токена
]