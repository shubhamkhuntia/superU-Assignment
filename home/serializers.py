from rest_framework import serializers
from .models import UserProfile


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

    def validate(self, data):
        special_characters = "!@#$%^&*()-+?_-,<>/"
        name = data.get('name')
        if name and any(c in special_characters for c in name):
            raise serializers.ValidationError(
                {'name': 'Name cannot contain special characters'})
        return data
