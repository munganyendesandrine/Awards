from django.db import models
from django.contrib.auth.models import User
# from tinymce.models import HTMLField

# Create your models here.

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    username=models.CharField(max_length =30)
    profile_photo = models.ImageField(upload_to = 'pic/')
    bio=models.CharField(max_length =30)
    # posted_projects = models.IntegerField()
    contacts=models.CharField(max_length =30)

    def __str__(self):
        return self.bio

    @classmethod
    def get_picture(cls,id):
        Profile.objects.all()


class Projects(models.Model):
   
    title=models.CharField(max_length =20)
    image_landing_page=models.ImageField(upload_to = 'picture/')
    detailed_description=models.CharField(max_length =60)
    link_to_livesite=models.CharField(max_length =30)

    def save_projects(self):
        self.save() 
    
    def __str__(self):
        return self.title
