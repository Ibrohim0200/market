from django.db import models
from common.models import BaseModel
from stores.models import Store

# Create your models here.

class Category(BaseModel):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="categories")
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "categories"
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}({self.store.name})"