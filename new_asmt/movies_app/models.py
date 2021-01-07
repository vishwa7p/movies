from django.db import models
# Create your models here.


class Poster(models.Model):
    poster = models.ImageField(null=True)

    def __str__(self):
        return str(self.poster)


class Movies(models.Model):
    poster = models.ForeignKey(Poster, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    director = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.poster)

