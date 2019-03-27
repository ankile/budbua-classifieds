from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from messages.models import Chat
from messages.models import Message
from messages.serializers import ChatListSerializer


class ChatListCreateView(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly,)

    @staticmethod
    def get(self, request):
        serializer = ChatListSerializer(context={'user': request.user})
        return Response(serializer.data, status=status.HTTP_200_OK)


    @staticmethod
    def post(request):
        serializer = ChatCreateSerializer(data=request.data, context={'user': request.user})

class ChatMessagesCreateView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    @staticmethod
    def get(self, request):
        serializer = ChatListSerializer(context={'user': request.user})
        return Response(serializer.data, status=status.HTTP_200_OK)


class AdsListCreateView(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly, )

    @staticmethod
    def get(request):

        print(request.GET)
        search_query = request.GET.get("search","")
        ads = Ad.objects.filter(title__icontains=search_query)
        serializer = AdListSerializer(ads, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request):
        serializer = AdCreateSerializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)