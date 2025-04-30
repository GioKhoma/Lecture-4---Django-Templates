from django.db import models

class Profile(models.Model):
    full_name = models.CharField(max_length=55)
    position = models.CharField(max_length=55)
    bio = models.TextField()

    def __str__(self):
        return self.full_name
