from django.db import models
from common.models import BaseModel
from account.models import User
from products.models import Product


class Order(BaseModel):
    PAYMENT_CHOICES = [
        ('cash', 'Naqd'),
        ('card', 'Karta'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    amount = models.PositiveIntegerField()
    date_of_order = models.DateTimeField(auto_now_add=True)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_CHOICES)

    class Meta:
        db_table = "orders"
        ordering = ['-date_of_order']
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"Order #{self.id} - {self.user.username} - {self.product.name}"
