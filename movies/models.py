from turtle import title
from django.db import models

class Actor(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    date_of_birth = models.DateField()
    movie = models.ManyToManyField("Movie", through="")

    class Meta:
        db_table = "actors"


class Movie(models.Model):
    title = models.CharField(max_length=45)
    release_date = models.DateField()
    running_time = models.IntegerField()

    class Meta:
        db_table = "movies"


class ActorsMovies(models.Model):
    actor = models.ForeignKey("Actor", on_delete=models.CASCADE)
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)









#allergy
class Allergy(models.Model):
    name = models.CharField(max_length=45)
    

    class Meta:
        db_table = "Allergy"

#drinks
class Drinks(models.Model):
    categories = models.ForeignKey('Categories', on_delete=models.CASCADE)
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    allergy = models.ManyToManyField(Allergy, through='Allergy_drink')
    
    class Meta:
        db_table = "Drinks"

#allergy_drink
class Allergy_drink(models.Model):
    allergy = models.ForeignKey("Allergy", on_delete=models.CASCADE)
    drink = models.ForeignKey('Drinks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Allergy_drink"