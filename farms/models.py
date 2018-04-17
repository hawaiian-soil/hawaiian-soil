from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.contrib.auth.models import User

from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

from localflavor.us.models import USStateField, USZipCodeField


# Create your models here.
class Farmer(AbstractUser):

    def __str__(self):
        return self.first_name + " " + self.last_name

    # username = models.CharField(max_length=30, unique=True)
    # password = models.CharField(max_length=30)
    # first_name = models.CharField(max_length=50, blank=True)
    # last_name = models.CharField(max_length=50, blank=True)
    # email = models.EmailField(blank=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    street_address = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=30, blank=True)
    state = USStateField(blank=True)
    zipcode = USZipCodeField(blank=True)

    # bio = models.TextField(max_length=500, blank=True)
    # location = models.CharField(max_length=30, blank=True)
    # birth_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender=AbstractUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Farmer.objects.create(user=instance)


@receiver(post_save, sender=AbstractUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=AbstractUser)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Farmer.objects.create(user=instance)
    instance.profile.save()


