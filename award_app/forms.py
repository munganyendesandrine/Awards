from django import forms
from .models import Profile,Projects,Rating

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        
class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = []

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        exclude = []
        # widgets = {
        #     'content': forms.CheckboxSelectMultiple(),
        # }
        # content=forms.CharField(widget=forms.Textarea)