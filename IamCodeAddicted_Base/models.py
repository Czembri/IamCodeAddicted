from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager

from django.conf import settings
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        if not username:
            raise ValueError('Users must have a username')

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self_db)
        return user



class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name="email" ,max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.email


    def has_module_perms(self, app_label):
        return True


class Movie(models.Model):
    name = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=10000)
    date_of_release = models.DateTimeField()
    image_url = models.URLField(max_length=300)
    rating = models.FloatField(null=False, default=5.0)
    price = models.FloatField(null=False, default=19.0)
    added_by = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return f'You are about to hit: {self.name}'

    class Meta:
        ordering = ['date_of_release']
        


class MoviesPurchase(models.Model):
    user = models.ForeignKey(
        CustomUser, related_name="users",on_delete=models.CASCADE, null=False
    )
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE, null=False, related_name="movies")
    date_of_purchase = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'User: {self.user} | Movie: {self.movie}'

    
    class Meta:
        ordering = ['date_of_purchase']

