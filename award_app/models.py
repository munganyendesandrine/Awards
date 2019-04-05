from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    username=models.CharField(max_length =30)
    profile_photo = models.ImageField(upload_to = 'pic/',null=True)
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
    image_landing_page=models.ImageField(upload_to = 'picture/',null=True)
    detailed_description=models.CharField(max_length =60)
    link_to_livesite=models.CharField(max_length =30)

    def save_projects(self):
        self.save() 
    
    @classmethod
    def get_pic(cls,id):
        Projects.objects.all()

    @classmethod
    def count_posts(cls,id):
        Projects.objects.all().count()

    def __str__(self):
        return self.title
    
    @classmethod
    def search_by_title(cls,search_term):
        images=Projects.objects.filter(title__icontains=search_term)
        return images 



class Rating2(models.Model):
   
    design_rate=models.IntegerField(
        default=0,
        validators=[MaxValueValidator(10), MinValueValidator(1)])
    # design_unlike=models.IntegerField()
    content_rate=models.IntegerField(
        default=0,
        validators=[MaxValueValidator(10), MinValueValidator(1)])
    # content_unlike=models.IntegerField()
    usability_rate=models.IntegerField(
        default=0,
        validators=[MaxValueValidator(10), MinValueValidator(1)])
    # usability_unlike=models.IntegerField()

    @classmethod
    def get_rates(cls,id):
        Rating2.objects.all()
    @classmethod
    def get_total(cls,id):
        Rating2.objects.all().sum()

    def save_rates2(self):
        self.save() 


