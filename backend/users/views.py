from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserSerializer, UserUpdateSerializer, UserCreateSerializer


class UserDetailView(APIView):

    permission_classes = (IsAuthenticated, )

    @staticmethod
    def get(request):
        serializer = UserSerializer(request.user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def put(request):
        serializer = UserUpdateSerializer(request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    @staticmethod
    def delete(_):
        request.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserCreateView(APIView):

    permission_classes = (AllowAny, )

    @staticmethod
    def post(request):
        print(request.data)
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
