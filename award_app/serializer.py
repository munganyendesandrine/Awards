from rest_framework import serializers
from .models import wingsdMerch

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = wingsdMerch
        fields = ('name', 'description', 'price')