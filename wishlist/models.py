from django.db import models
from products.models import Product
from profiles.models import Profile


class Wishlist(models.Model):

    user = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='wishlist')
    products = models.ManyToManyField(Product, blank=True, related_name='wishlist')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Wishlist'
        verbose_name_plural = 'Wishlists'

    def __str__(self):
        """Return wishlist username."""
        return f'{self.user.username} wishlist'
    
    def add(self, product):
        """Add product to wishlist."""
        if product not in self.products.all():
            self.products.add(product)
            return True
        return False
    
    def remove_from_wishlist(self, product):
        """Remove product from wishlist."""
        if product in self.products.all():
            self.products.remove(product)
            return True
        return False
    
    def clear_wishlist(self):
        """Clear wishlist."""
        self.products.clear()
        return True
    
    def get_products(self):
        """Return all products in wishlist."""
        return self.products.all()