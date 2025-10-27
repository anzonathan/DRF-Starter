from django.contrib.auth.models import Group, User
from rest_framework import serializers 

class UserSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url","username","email","groups"]
    
class GroupSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


        
