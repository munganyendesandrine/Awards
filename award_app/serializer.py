from rest_framework import serializers
from .models import Profile,Projects

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'username', 'bio', 'contacts')


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('title', 'detailed_description', 'link_to_livesite')

 