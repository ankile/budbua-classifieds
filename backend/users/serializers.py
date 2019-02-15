from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)


class BaseUserSerializer(serializers.ModelSerializer):
    def validate(self, data, *args, **kwargs):

        if 'password' in data and not len(data['password']):
            data.pop('password')

        if 'password' in data and len(data['password']):
            if 'password2' not in data:
                raise serializers.ValidationError(
                    {'password2': ['This field must be filled out when setting the password']})

            if data['password'] != data['password2']:
                raise serializers.ValidationError({'password2': ['Confirmation does not match the password']})

            try:
                validate_password(data['password'])
            except ValidationError as e:
                raise serializers.ValidationError(
                    {'password': list(map(lambda x: str(x).strip("[]'"), e.error_list))})

        elif not self.instance.password:
            raise serializers.ValidationError({'password': ['You must choose a password']})

        return super().validate(data)


class UserCreateSerializer(BaseUserSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'password2')

    def validate(self, data, *args, **kwargs):
        if 'password' not in data:
            raise serializers.ValidationError(["You must provide a password when signing up."])

        return super().validate(data, *args, **kwargs)

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create(**validated_data)
        user.set_password(validated_data.pop('password'))

        return user


class UserUpdateSerializer(BaseUserSerializer):

    password = serializers.CharField(write_only=True, required=False)
    password2 = serializers.CharField(write_only=True, required=False)

    def update(self, instance, validated_data):

        if 'password' in validated_data:
            instance.set_password(validated_data.pop('password'))
            validated_data.pop('password2')

        return super().update(instance, validated_data)
