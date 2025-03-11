# animals/admin.py

from django.contrib import admin
from .models import Animal

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'age', 'weight')
    list_filter = ('name', 'species')
    search_fields = ('name', 'species')