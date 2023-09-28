from django.db import models


class CatalogPatrioticMusic(models.Model):
    fullname = models.CharField(max_length=200)
    composer = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    theme = models.CharField(max_length=200)
    creationyear = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.fullname} *** {self.composer} *** {self.genre} *** {self.theme} *** {self.creationyear}"
