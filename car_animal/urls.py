from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('car/', include('car.urls')),
    path('animal/', include('animal.urls')),
]