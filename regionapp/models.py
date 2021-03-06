from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
from django.dispatch import receiver
from django.db.models.signals import post_save


class NeighbourHood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=60)
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='hood')
    image = models.ImageField(upload_to='images/', default='default.png')
    health_tell = models.IntegerField(null=True, blank=True)
    police_number = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True)
    Occupants_Count = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return f'{self.name} region'

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)
    
          
    def update_neighbourhood(self):
        self.update()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=80, blank=True)
    profile_picture = models.ImageField(upload_to='images/', default='default.png')
    location = models.CharField(max_length=50, blank=True, null=True)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)
    email = models.CharField(max_length=80, blank=True)
   

    def __str__(self):
        return f'{self.user.username }Profile'
    
    def save_Profile(self):
        self.save()
        
    def delete_Profile(self):
        self.delete()
        
    def update_Profile(self):
        self.update()

    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Business(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    business_picture = models.ImageField(upload_to='images/',null=True)
    description = models.TextField(blank=True)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, related_name='business')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner')

    def __str__(self):
        return f'{self.name} Business'

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(name__icontains=name).all()

    
class Post(models.Model):
    title = models.CharField(max_length=120, null=True)
    post = models.TextField()
    picture = models.ImageField(upload_to='posts/', null=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_owner')
    region = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, related_name='region_post')


    def __str__(self):
        return self.title
    
    def save_post(self):
        self.save()
        
    def delete_post(self):
        self.delete()
        
    def update_post(self):
        self.update()