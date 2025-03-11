from django.db import models

class Animal(models.Model):
    SPECIES_CHOICES = [
        ('mammal', 'ძუძუმწოვარი'),
        ('bird', 'ფრინველი'),
        ('reptile', 'რეპტილია'),
        ('fish', 'თევზი'),
        ('insect', 'მწერი'),
    ]

    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50, choices=SPECIES_CHOICES)
    age = models.IntegerField()
    weight = models.DecimalField(max_digits=6, decimal_places=2, help_text="Weight in kg")
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.species})"