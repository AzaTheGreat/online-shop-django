from django.contrib.auth.models import User
from django.db import models

from store.models import Item


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='carts',
        verbose_name='Customer',
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Date of Creation',)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    @property
    def total_price(self):
        total_price = sum(item.total_price for item in self.items.all())
        return total_price

    def __str__(self):
        return f"Cart {self.id} for {self.user.username}"

    def clear(self):
        self.items.all().delete()


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='Cart',
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        verbose_name='Item',
    )
    quantity = models.PositiveIntegerField(
        default=1, verbose_name='Quantity',)

    class Meta:
        verbose_name = 'Item in cart'
        verbose_name_plural = 'Items in cart'

    @property
    def total_price(self):
        total_price = self.quantity * self.item.price
        return total_price

    def __str__(self):
        return f"{self.quantity} x {self.item.title}"
