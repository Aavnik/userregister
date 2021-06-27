from django.db import models
from django.contrib.auth.models import User, AbstractUser
from .manager import *
from .threads import *
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Homeuser(AbstractUser):
    username = None
    email = models.EmailField(unique = True)
    phone = models.CharField(max_length = 12)
    emailtoken = models.CharField(max_length = 200)
    is_verified = models.BooleanField(default = False)
    is_deleted = models.BooleanField(default = False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    

@receiver(post_save, sender=User)
def send_verification_mail(sender,instance,created, **kwargs):
    if created:
        emailID = instance.email
        verifyToken = instance.emailtoken
        thread_obj = Send_mail_thread(emailID,verifyToken)
        thread_obj.start()

