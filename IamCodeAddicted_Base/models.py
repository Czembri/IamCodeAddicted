from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    name = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=10000)
    date_of_release = models.DateTimeField()
    image_url = models.URLField(max_length=300)
    added_by = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return f'You are about to hit: {self.name}'

    class Meta:
        ordering = ['date_of_release']
        


class MoviesPurchase(models.Model):
    user = models.ForeignKey(
        User, related_name="users",on_delete=models.CASCADE, null=False
    )
    movie = models.ForeignKey(
        Movie, related_name="movies",on_delete=models.CASCADE, null=False
    )
    date_of_purchase = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'User: {self.user} | Movie: {self.movie}'

    
    class Meta:
        ordering = ['date_of_purchase']