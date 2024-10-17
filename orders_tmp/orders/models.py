from django.conf import settings
from django.db import models

from products.models import Product

# Create your models here.
class Cart(models.Model):
    """
    Modelo que representa el carrito de compras de un usuario.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Carrito de {self.user.username}"

class CartItem(models.Model):
    """
    Modelo que representa un ítem dentro del carrito.
    """
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

class Order(models.Model):
    """
    Modelo que representa una orden realizada por un usuario.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('pending','Pending'), ('processed', 'Processed'), ('shipped', 'Shipped'), ('completed', 'Completed'), ('canceled', 'Canceled')], default='pending')
    
    def __str__(self):
        return f"Orden {self.id} de {self.user.username}"

class OrderItem(models.Model):
    """
    Modelo que representa un ítem dentro de una orden.
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Orden{self.order.id})"