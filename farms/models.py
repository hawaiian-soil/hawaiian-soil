from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Farmer(models.Model):

    def __str__(self):
        return self.name

    username = models.OneToOneField(User, on_delete=models.CASCADE)
    fist_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def update_farmer_profile(sender, instance, created, **kwargs):
    if created:
        Farmer.objects.create(user=instance)
    instance.profile.save()


