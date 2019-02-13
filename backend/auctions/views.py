from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from auctions.models import Ad
from auctions.serializers import AdSerializer


class AdsListCreateView(APIView):

    permission_classes = (AllowAny, )

    def get(self, request):

        ads = Ad.objects.all()[:25]
        serializer = AdSerializer(ads, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class AdsDetailView(APIView):
    pass
