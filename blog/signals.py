from django.dispatch import Signal
from django.db.models.signals import post_save,pre_save,pre_delete
from django.contrib.auth.models import User
from django.contrib.auth import user_logged_in,user_logged_out
from django.dispatch import receiver
from django.contrib.admin.models import LogEntry
from .models import Post,activities

new_post= Signal(providing_args=["Post"])
delete_post=Signal(providing_args=["Post"])
# updated_post=Signal(providing_args=["Post"])

@receiver(post_save,sender=Post)
def activites(sender,instance,**kwargs):
    activities.objects.create(username=instance.author,details='Has created a new blog post.')

@receiver(pre_delete,sender=Post)
def posts_delete(sender,instance,**kwargs):
    activities.objects.create(username=instance.author,details='Has deleted a blog post.')

# @receiver(post_save,sender=Post)
# def activites(sender,instance,**kwargs):
#     activities.objects.create(username=instance.author,details='has updated a new blog post')