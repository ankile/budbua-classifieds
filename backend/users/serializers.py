from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email',)


class BaseUserSerializer(serializers.ModelSerializer):
    def validate(self, data, *args, **kwargs):

        print(data)

        if 'password_2' not in data:
            raise serializers.ValidationError(
                {'password_2': ['This field must be filled out when setting the password']})

        if data['password'] != data['password_2']:
            raise serializers.ValidationError({'password_2': ['Confirmation does not match the password']})

        try:
            validate_password(data['password'])
        except ValidationError as e:
            raise serializers.ValidationError(
                {'password': list(map(lambda x: str(x).strip("[]'"), e.error_list))})

        return super().validate(data)


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'password_2')

    def validate(self, data, *args, **kwargs):
        if 'password' not in data:
            raise serializers.ValidationError(
                {'password': ['You must provide a password when signing up.']})

        if 'password_2' not in data:
            raise serializers.ValidationError(
                {'password_2': ['This field must be filled out when setting the password']})

        if data['password'] != data['password_2']:
            raise serializers.ValidationError({'password_2': ['Confirmation does not match the password']})

        try:
            validate_password(data['password'])
        except ValidationError as e:
            raise serializers.ValidationError(
                {'password': list(map(lambda x: str(x).strip("[]'"), e.error_list))})

        return super().validate(data)

    def create(self, validated_data):
        validated_data.pop('password_2')
        user = User.objects.create(**validated_data)
        user.set_password(validated_data.pop('password'))
        user.save()

        return user


class UserUpdateSerializer(BaseUserSerializer):

    password = serializers.CharField(write_only=True, required=False)
    password_2 = serializers.CharField(write_only=True, required=False)

    def update(self, instance, validated_data):

        if 'password' in validated_data:
            instance.set_password(validated_data.pop('password'))
            validated_data.pop('password_2')

        return super().update(instance, validated_data)
