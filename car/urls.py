from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.CarList.as_view(), name='car-list'),
    path('cars/<int:pk>/', views.CarDetail.as_view(), name='car-detail'),
]