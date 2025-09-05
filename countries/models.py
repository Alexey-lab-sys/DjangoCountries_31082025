from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    languages = models.JSONField()

    def __str__(self):
        return self.name