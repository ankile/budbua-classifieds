from rest_framework import serializers

from user_messages.models import Chat, Message


class ChatListSerializer(serializers.ModelSerializer):
    display_name = serializers.SerializerMethodField()

    class Meta:
        model = Chat
        fields = ('id', 'display_name', 'latest_message', 'updated_at', 'message_count')

    def get_display_name(self, chat):
        return ", ".join(map(lambda c: c.name, chat.users.exclude(pk=self.context['user'].id)))


class MessageListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('sender', 'message', 'created_at', 'chat')
