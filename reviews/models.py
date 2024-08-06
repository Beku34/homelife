from django.db import models
from django.contrib.auth.models import User
from config import settings
from product.models import Product


class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='rating')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    rating = models.PositiveIntegerField(choices=((1, '1 star'), (1.5, '1.5 stars'), (2, '2 stars'), (2.5, '2.5 stars'), (3, '3 stars'), (3.5, '3.5 star'), (4, '4 stars'), (4.5, '4.5 stars'), (5, '5 stars')))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('product', 'user')

    def __str__(self):
        return f"{self.user}'s {self.rating}-star rating for {self.product}"
