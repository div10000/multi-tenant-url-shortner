from django.db import models

# Create your models here.
class Tenant(models.Model):
    name = models.CharField(max_length=100)
    domain = models.CharField(max_length=255, unique=True)
    app_name = models.CharField(max_length=100)
    logo_url = models.URLField()
    primary_color = models.CharField(max_length=20)

    def __str__(self):
        return self.name