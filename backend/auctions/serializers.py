from rest_framework import serializers

from auctions.models import Ad, Bid
from budbua.utils.validators import try_cast_to_int


class AdListSerializer(serializers.ModelSerializer):
    user_max_bid = serializers.SerializerMethodField()

    class Meta:
        model = Ad
        read_only_fields = ('maximum_bid', 'num_bids')
        fields = ('id', 'title', 'description', 'bid_end_time', 'minimum_bid', 'maximum_bid', 'num_bids', 'owner',
                  'highest_bidder', 'user_max_bid', 'image_string')

    def get_user_max_bid(self, ad):
        return ad.user_max_bid


class AdCreateSerializer(serializers.ModelSerializer):
    minimum_bid = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Ad
        fields = ('title', 'description', 'bid_end_time', 'minimum_bid', 'image_string',)

    @staticmethod
    def validate_minimum_bid(value):
        value = try_cast_to_int(value)

        if value < 0:
            raise serializers.ValidationError(f"Bids cannot be negative, value={value}, given.")

        return value

    def create(self, validated_data):
        validated_data['owner'] = self.context['user']
        return super().create(validated_data)


class AdDetailSerializer(serializers.ModelSerializer):
    user_max_bid = serializers.SerializerMethodField()

    class Meta:
        model = Ad
        read_only_fields = ('first_name', 'last_name', 'email',)
        fields = ('id', 'title', 'description', 'bid_end_time', 'minimum_bid', 'maximum_bid', 'num_bids', 'owner',
                  'image_string', 'highest_bidder', 'user_max_bid') + read_only_fields

    def get_user_max_bid(self, ad):
        return ad.user_max_bid


class BidSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('bidder', 'ad', 'value')
        model = Bid
