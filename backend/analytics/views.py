# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from analytics.permissions import IsOwner
from auctions.models import Ad, Bid
from users.models import User


class OwnerAnalyticsView(APIView):

    permission_classes = (IsOwner, )

    @staticmethod
    def get(_):

        data = {
            'user_count': User.objects.all().count(),
            'ad_count': Ad.objects.all().count(),
            'bid_count': Bid.objects.all().count(),
            'report_count': 0  # TODO: Implement report count when ready
        }

        return Response(data=data, status=status.HTTP_200_OK)
