from django.db import models
from django.core.exceptions import ValidationError 
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
            
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.email

class Country(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=3, unique=True)
    curr_symbol = models.CharField(max_length=10, blank=True, null=True)
    phone_code = models.CharField(max_length=5, blank=True, null=True, unique=True)
    my_user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="countries")

    class Meta:
        db_table = 'country'
        constraints = [
            models.UniqueConstraint(fields=['my_user', 'name'], name='unique_country_per_user')
        ]

    def __str__(self):
        return self.name

class State(models.Model):
    id = models.UUIDField(primary_key=True)
    state_code = models.CharField(max_length=3, blank=True, null=True)
    gst_code = models.CharField(max_length=15, blank=True, null=True,unique=True)
    name = models.CharField(max_length=100)
    country = models.ForeignKey("Country", on_delete=models.CASCADE, related_name="states")

    class Meta:
        db_table = 'state'
        constraints = [
            models.UniqueConstraint(fields=['country', 'name'], name='unique_state_per_country')
        ]

    def __str__(self):
        return self.name
        

class City(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    city_code = models.CharField(max_length=10, blank=True, null=True)
    phone_code = models.CharField(max_length=10, blank=True, null=True, unique=True)
    population = models.BigIntegerField(blank=True, null=True)
    avg_age = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    num_of_adult_males = models.BigIntegerField(blank=True, null=True)
    num_of_adult_females = models.BigIntegerField(blank=True, null=True)
    state = models.ForeignKey("State", on_delete=models.CASCADE, related_name="cities")

    class Meta:
        db_table = 'city'
        constraints = [
            models.UniqueConstraint(fields=['state', 'name'], name='unique_city_per_state'),
            models.UniqueConstraint(fields=['state', 'city_code'], name='unique_city_code_per_state'),
        ]

    def clean(self):
        if (
            self.population is not None
            and self.num_of_adult_males is not None
            and self.num_of_adult_females is not None
        ):
            if self.population < (self.num_of_adult_males + self.num_of_adult_females):
                raise ValidationError("Population must be greater than or equal to sum of adult males and females.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
            return self.name
