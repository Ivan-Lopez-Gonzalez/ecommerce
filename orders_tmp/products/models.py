from django.db import models

# Create your models here.
class Category(models.Model):
    """
    Categoría a la que pertenece un producto.
    """
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    """
    Modelo que representa un producto en el ecommerce.
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category,
    on_delete=models.SET_NULL, null=True, related_name='products')
    image = models.ImageField(upload_to='product_images/',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name