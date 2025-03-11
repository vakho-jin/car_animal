from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'color', 'price', 'is_available')
    list_filter = ('brand', 'year', 'is_available')
    search_fields = ('brand', 'model')