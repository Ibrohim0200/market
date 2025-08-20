from django.db import models
from common.models import BaseModel
from account.models import User
from products.models import Product


class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cart_products")
    amount = models.PositiveIntegerField()

    class Meta:
        db_table = "cart"
        verbose_name = "Cart"
        verbose_name_plural = "Carts"
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user} - {self.product.name} x {self.amount}"
