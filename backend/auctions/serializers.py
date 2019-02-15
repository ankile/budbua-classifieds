from rest_framework import serializers

from auctions.models import Ad, Bid
from budbua.utils.validators import try_cast_to_int


class AdListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        read_only_fields = ('maximum_bid', 'num_bids')
        fields = ('id', 'title', 'description', 'bid_end_time', 'minimum_bid', 'maximum_bid', 'num_bids', 'owner', )


class AdCreateSerializer(serializers.ModelSerializer):

    minimum_bid = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Ad
        fields = ('title', 'description', 'bid_end_time', 'minimum_bid', )

    @staticmethod
    def validate_minimum_bid(value):
        value = try_cast_to_int(value)

        if value < 0:
            raise serializers.ValidationError(f"Bids cannot be negative, value={value}, given.")

        return value

    def create(self, validated_data):
        user = self.context['user']

        minimum_bid = validated_data.pop('minimum_bid', None) or 0
        ad = Ad.objects.create(**validated_data, owner=user)
        Bid.objects.create(ad=ad, value=minimum_bid)

        return ad


class AdDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        read_only_fields = ('first_name', 'last_name', 'email', )
        fields = ('id', 'title', 'description', 'bid_end_time', 'minimum_bid', 'maximum_bid', 'num_bids', 'owner', ) \
            + read_only_fields
        extra_kwargs = {

        }

