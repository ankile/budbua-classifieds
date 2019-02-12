from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.Serializer):

    username = serializers.CharField()
    email = serializers.EmailField()

    class Meta:
        fields = ('username', 'email')
        model = User
