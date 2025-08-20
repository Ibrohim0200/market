from django.db import models

# Create your models here.
class BaseModel(models.Model):
    """
    An abstract base model that provides common fields for all models.
    """
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        abstract = True