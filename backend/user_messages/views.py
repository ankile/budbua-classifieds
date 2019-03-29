from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from user_messages.models import Chat, Message
from user_messages.serializers import ChatListSerializer, MessageListCreateSerializer


class ChatListCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request):
        chats = Chat.objects.filter(users__id=request.user.id)
        serializer = ChatListSerializer(chats, many=True, context={'user': request.user})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request):
        receivers = request.data.get('receivers')

        if receivers is None:
            return Response('Receivers argument must be present', status=status.HTTP_400_BAD_REQUEST)

        if not isinstance(receivers, list):
            receivers = [receivers]

        try:
            chat = Chat.objects.create()
            chat.users.set(receivers + [request.user.id])
            chat.save()
        except ValueError:
            return Response('Receivers argument must be int or list of ints', status=status.HTTP_400_BAD_REQUEST)

        return Response(data={"id": chat.id}, status=status.HTTP_201_CREATED)


class MessagesListCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request, chat_pk):
        messages = Message.objects.filter(chat_id=chat_pk)
        serializer = MessageListCreateSerializer(messages, many=True, context={'user': request.user})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request, chat_pk):
        try:
            chat = Chat.objects.get(pk=chat_pk, users__id=request.user.id)
        except ObjectDoesNotExist:
            return Response('Not valid chat ID for this user', status=status.HTTP_400_BAD_REQUEST)

        serializer = MessageListCreateSerializer(data={**request.data, "chat": chat.id, "sender": request.user.id})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)
