from django import forms
from .models import Profile,Projects,Rating2

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
        model = Rating2
        exclude = []
        # widgets = {
        #     'content': forms.CheckboxSelectMultiple(),
        # }
        # content=forms.CharField(widget=forms.Textarea)