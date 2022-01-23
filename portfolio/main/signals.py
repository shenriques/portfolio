from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from . models import UserProfile

'''

When you create a User from Authentication Models (or do it via terminal), a signal is sent
It's received here where the function creates a main models User Profile
E.g. creating a superuser will create a user profile with those details

'''

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		userprofile = UserProfile.objects.create(user=instance)