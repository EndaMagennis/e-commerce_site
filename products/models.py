from django.db import models

# choices
DIFFICULTY_CHOICES = [
    (1, 'Easy'),
    (2, 'Medium'),
    (3, 'Hard'),
]

PLAYER_CHOICES = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
]

PLAY_TIME_CHOICES = [
    (15, '15'),
    (30, '30'),
    (45, '45'),
    (60, '60'),
    (90, '90'),
    (120, '120'),
    (150, '150'),
    (180, '180'),
]

MINIMUM_AGE_CHOICES = [
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
    (11, '11'),
    (12, '12'),
    (13, '13'),
    (14, '14'),
    (15, '15'),
    (16, '16'),
    (17, '17'),
    (18, '18'),
]

class Category(models.Model):
    """Model for a category of products in the store"""

    name = models.CharField(max_length=255)
    friendly_name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name
    

class Product(models.Model):
    """Model for a product in the store"""

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254, unique=True)
    description = models.TextField(null=True, blank=True)
    detailed_description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    min_players = models.CharField(choices=PLAYER_CHOICES, max_length=254, null=True, blank=True, default="1")
    max_players = models.CharField(choices=PLAYER_CHOICES, max_length=254, null=True, blank=True, default="1")
    play_time = models.CharField(choices=PLAY_TIME_CHOICES, max_length=254, null=True, blank=True, default="15")
    age = models.CharField(choices=MINIMUM_AGE_CHOICES, max_length=254, null=True, blank=True, default="3")
    difficulty = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    year_published = models.IntegerField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    def generate_sku(self):
        return self.name.replace(" ", "-").lower()
    
    def check_min_players_max_players(self):
        if self.min_players > self.max_players:
            return False
        return True
    