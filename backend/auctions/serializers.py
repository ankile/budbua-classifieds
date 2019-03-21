from rest_framework import serializers

from auctions.models import Ad, Bid
from budbua.utils.validators import try_cast_to_int


class AdListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        read_only_fields = ('maximum_bid', 'num_bids')
        fields = ('id', 'title', 'description', 'bid_end_time', 'minimum_bid', 'maximum_bid', 'num_bids', 'owner',
                  'highest_bidder', 'image_string', 'zip_code')


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


class AdDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        read_only_fields = ('first_name', 'last_name', 'email', )
        fields = ('id', 'title', 'description', 'bid_end_time', 'minimum_bid', 'maximum_bid', 'num_bids', 'owner',
                  'image_string', 'highest_bidder', 'zip_code') + read_only_fields


class BidSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('bidder', 'ad', 'value')
        model = Bid




