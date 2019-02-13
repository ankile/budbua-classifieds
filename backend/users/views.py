from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserSerializer


class UsersListCreateView(APIView):

    permission_classes = [AllowAny]

    def get(self, request):

        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

