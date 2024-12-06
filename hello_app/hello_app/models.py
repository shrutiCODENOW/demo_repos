from django.db import models

class PersonModel(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()

    def __str__(self):
        return self.title