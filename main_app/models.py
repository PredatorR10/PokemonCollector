from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GENDER_CHOICES = (
    ("M", "Male"),
    ("F", "Female")
)

class PokemonFood(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Pokemon(models.Model):

    name = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    img = models.CharField(max_length=250)
    level = models.IntegerField()
    gender = models.CharField(max_length=10, choices = GENDER_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pokemonfood = models.ManyToManyField(PokemonFood)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']