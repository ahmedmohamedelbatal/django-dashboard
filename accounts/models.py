from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Profile(models.Model):
  gender = {
    ('Male','Male'),
    ('Female','Female')
  }
  user = models.OneToOneField(User , on_delete=models.CASCADE)
  job = models.CharField(max_length=100, default='not found')
  address = models.CharField(max_length=100, default='not found')
  gender = models.CharField(max_length=100, choices=gender, default='not found')
  phone = models.CharField(max_length=12, default='not found')
  image = models.ImageField(upload_to='profiles/')
  biography = models.TextField(max_length=300, default='not found')
  
  def __str__(self):
    return str(self.user)

@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
  if created: 
    Profile.objects.create(user = instance)