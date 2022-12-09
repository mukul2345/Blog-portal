from blog.views import activity
from django.dispatch import Signal
from django.contrib.auth import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from blog.models import activities

new_user=Signal(providing_args=["User"])
@receiver(post_save,sender=User)
def user_new(sender,instance,**kwargs):
    activities.objects.create(username=instance.username,details='Has been registered as a new user.')  

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()
               