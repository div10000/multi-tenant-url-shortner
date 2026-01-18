from django.db import models
from tenants.models import Tenant

# Create your models here.
class ShortURL(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.short_code
