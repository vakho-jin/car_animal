from django.urls import path
from . import views

urlpatterns = [
    path('animals/', views.AnimalList.as_view(), name='animal-list'),
    path('animals/<int:pk>/', views.AnimalDetail.as_view(), name='animal-detail'),
]