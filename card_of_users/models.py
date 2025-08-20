from django.db import models
from django.conf import settings

class CardOfUsers(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cards")
    card_number = models.CharField(max_length=16)
    expire_date = models.CharField(max_length=5)

    class Meta:
        db_table = "card_of_users"
        verbose_name = "User Card"
        verbose_name_plural = "User Cards"

    def __str__(self):
        return f"{self.user.username} - **** **** **** {self.card_number[-4:]}"
