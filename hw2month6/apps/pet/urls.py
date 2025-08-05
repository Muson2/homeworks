from django.urls import path
from .views import RegisterView, PetListCreateView, PetDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('pets/', PetListCreateView.as_view(), name='pet-list-create'),
    path('pets/<int:pk>/', PetDetailView.as_view(), name='pet-detail'),
]
