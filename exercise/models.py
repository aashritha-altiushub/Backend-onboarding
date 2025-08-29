from django.db import models
from django.contrib.auth.models import AbstractUser

class User(models.Model):
    id = models.UUIDField(primary_key=True)
    email = models.EmailField(unique=True)    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'user'

class Country(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=3, unique=True)
    curr_symbol = models.CharField(max_length=10, blank=True, null=True)
    phone_code = models.CharField(max_length=5, blank=True, null=True)
    my_user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="countries")

    class Meta:
        db_table = 'country'

class State(models.Model):
    id = models.UUIDField(primary_key=True)
    state_code = models.CharField(max_length=3, blank=True, null=True)
    gst_code = models.CharField(max_length=15, blank=True, null=True)
    name = models.CharField(max_length=100)
    country = models.ForeignKey("Country", on_delete=models.CASCADE, related_name="states")

    class Meta:
        db_table = 'state'
        

class City(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    city_code = models.CharField(max_length=10, blank=True, null=True)
    phone_code = models.CharField(max_length=10, blank=True, null=True)
    population = models.BigIntegerField(blank=True, null=True)
    avg_age = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    num_of_adult_males = models.BigIntegerField(blank=True, null=True)
    num_of_adult_females = models.BigIntegerField(blank=True, null=True)
    state = models.ForeignKey("State", on_delete=models.CASCADE, related_name="cities")

    class Meta:
        db_table = 'city'
