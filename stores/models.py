from django.conf import settings
from django.db import models
from common.models import BaseModel

class Store(BaseModel):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='stores/', blank=True, null=True)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='stores'
    )


    class Meta:
        db_table = 'stores'
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'

    def __str__(self):
        return self.name
