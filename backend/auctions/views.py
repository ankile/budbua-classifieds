from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from auctions.models import Ad
from auctions.serializers import AdSerializer


class AdsListCreateView(APIView):

    # TODO Change permission class to disallow unauthenticated users
    permission_classes = (AllowAny, )

    # TODO Implement searching and pagination
    def get(self, request):

        ads = Ad.objects.all()[:25]
        serializer = AdSerializer(ads, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AdSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)


class AdsDetailView(APIView):
    pass
