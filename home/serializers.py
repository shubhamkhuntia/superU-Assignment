from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.models import User


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):

        if data['username']:
            if User.objects.filter(username=data['username']).exists():
                raise serializers.ValidationError('username is taken')

        if data['email']:
            if User.objects.filter(email=data['email']).exists():
                raise serializers.ValidationError('email is taken')

        return data

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
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
