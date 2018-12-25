from django.db import models

class Good(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
