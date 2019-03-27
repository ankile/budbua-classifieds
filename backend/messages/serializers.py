from rest_framework import serializers

from messages.models import Chat, Message
from budbua.utils.validators import try_cast_to_int


class ChatListSerializer(serializers.ModelSerializer):

    display_name = serializers.SerializerMethodField()

    class Meta:
        model = Chat
        # read_only_fields = ('maximum_bid', 'num_bids')
        fields = ('id', 'display_name', 'latest_message', 'updated_at')

    def get_display_name(self):
        return ", ".join(list(self.instance.users.exclude(pk=self.context['user'].id).values_list('name', flat=True)))


class ChatCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = ()




class AdCreateSerializer(serializers.ModelSerializer):

    minimum_bid = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Ad
        fields = ('title', 'description', 'bid_end_time', 'minimum_bid', 'image_string', 'zip_code')

    @staticmethod
    def validate_minimum_bid(value):
        value = try_cast_to_int(value)

        if value < 0:
            raise serializers.ValidationError(f"Bids cannot be negative, value={value}, given.")

        return value

    @staticmethod
    def validate_zip_code(value):
        if not (value.isdigit() and len(value) == 4):
            raise serializers.ValidationError(f"Zip code must consist of numbers and be of length 4, value={value}.")

        return value

    def create(self, validated_data):
        validated_data['owner'] = self.context['user']
        return super().create(validated_data)