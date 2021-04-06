from .models import Profile,Post,Comment,Location,technologies
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields='__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields='__all__'


class technologiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = technologies
        fields='__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields='__all__'
