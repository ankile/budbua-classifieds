from rest_framework import serializers

from auctions.models import Ad
from users.models import User


class AdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        read_only_fields = ('maximum_bid', 'num_bids')
        fields = ('id', 'title', 'description', 'bid_end_time', 'minimum_bid', 'maximum_bid', 'num_bids', 'owner', )
