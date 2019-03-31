# Create your views here.
from collections import Counter
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from analytics.permissions import IsOwner
from auctions.models import Ad, Bid
from reports.models import AdReport, UserReport
from users.models import User


def cast_date(datetime):
    return datetime.strftime('%Y-%m-%d')


def objectify(item):
    return {'x': item[0], 'y': item[1]}


def create_cumulative_date_histogram(model):
    data = list(
        map(objectify,
            Counter(map(cast_date, model.objects.values_list('created_at', flat=True).order_by('created_at'))).items()))

    for i, item in enumerate(data[1:]):
        item['y'] += data[i]['y']

    return data


class OwnerAnalyticsView(APIView):
    permission_classes = (IsOwner,)

    @staticmethod
    def get(_):
        data = {
            'user_count': User.objects.all().count(),
            'ad_count': Ad.objects.all().count(),
            'bid_count': Bid.objects.all().count(),
            'report_count': AdReport.objects.all().count() + UserReport.objects.all().count(),
            'user_development': create_cumulative_date_histogram(User),
            'ad_development': create_cumulative_date_histogram(Ad),
        }

        return Response(data=data, status=status.HTTP_200_OK)
