from rest_framework import serializers

from auctions.models import Ad


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ('id', 'title', 'description', 'bid_end_time', 'minimum_bid', 'maximum_bid', )
