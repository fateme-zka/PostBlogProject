from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile


# HOW SIGNALS WORKS ?!
# when the user is saved then send this signal(post_save) and then this signal will receive by
# this receiver 👇 and this receiver is this create_profile function
# this function takes all of this arguments that out post_save signal pass to it
# and of course this function will run tasks which are in it.
@receiver(signal=post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:  # if the user has been created
        Profile.objects.create(user=instance)  # create profile for that user


@receiver(signal=post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    # instance would be the user
    instance.profile.save()
