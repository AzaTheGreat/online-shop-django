from django.contrib.auth.models import User
from django.db import models

from store.models import Item


class Order(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cash_courier', 'Cash to courier'),
        ('card_courier', 'Card to courier'),
        ('card_online', 'Card online'),
    ]
    STATUS_CHOICES = [
        ('created', 'Created'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled'),
    ]
    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD_CHOICES,
        verbose_name='Payment method',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='Customer',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date of Creation',
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='created',
        verbose_name='Status',
    )

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['-created_at']

    @property
    def total_price(self):
        total_price = sum(
            order_item.total_price for order_item in self.items.all())
        return total_price

    def __str__(self):
        return f"Order number {self.id} for {self.user}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='Order',
    )
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, verbose_name='Item',)
    quantity = models.PositiveIntegerField(
        default=1, verbose_name='Quantity',)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Price',)

    class Meta:
        verbose_name = 'Ordered product'
        verbose_name_plural = 'Ordered products'

    @property
    def total_price(self):
        total_price = self.quantity * self.item.price
        return total_price

    def __str__(self):
        return f"{self.quantity} x {self.item.title} in Order {self.order.id}"


class ShippingAddress(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Name',)
    last_name = models.CharField(max_length=50, verbose_name='Surname',)
    email = models.EmailField(verbose_name='Email',)
    phone = models.CharField(max_length=20, verbose_name='Phone Number',)
    address_line_1 = models.CharField(max_length=200, verbose_name='Address',)
    address_line_2 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Address (additional)',)
    order = models.OneToOneField(
        Order, on_delete=models.CASCADE, related_name='shipping_address', verbose_name='Order',)

    class Meta:
        verbose_name = 'Delivery address'
        verbose_name_plural = 'Delivery addresses'

    def __str__(self):
        return f"""
        {self.address_line_1} {self.address_line_2}
        For: {self.first_name} {self.last_name},
        Email: {self.email},
        Phone Number: {self.phone}
        """
