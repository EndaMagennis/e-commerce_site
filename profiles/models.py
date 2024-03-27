from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    A user profile model for maintaining user information
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = models.CharField(max_length=40, null=True, blank=True)
    profile_picture = models.ImageField(null=True, blank=True)
    profile_picture_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.user.username
    
    def get_full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        """
        Create or update the user profile
        """
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()
