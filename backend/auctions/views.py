from django.db.models import Max, Q, Count
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Bid, User
from .serializers import BidSerializer

from auctions.models import Ad
from auctions.serializers import AdCreateSerializer, AdListSerializer, AdDetailSerializer
from budbua.utils.mixins import ModelView


class AdsListCreateView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    # TODO Implement searching and pagination
    @staticmethod
    def get(request):
        search_query = request.GET.get("search", "")

        filter_query = request.GET.get("filter", None)

        ads = Ad.objects.filter(title__icontains=search_query).annotate(
            user_max_bid=Max('bids__value', filter=Q(bids__bidder=request.user)))

        if filter_query is not None:
            if filter_query == "MY_ADS":
                ads = ads.filter(owner=request.user)  # filter ads created by user

            elif filter_query == "MY_BIDS":
                ads = ads.filter(bids__bidder=request.user)

        serializer = AdListSerializer(ads, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request):
        serializer = AdCreateSerializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)


class AdsDetailView(ModelView):
    model = Ad
    permission_classes = (IsAuthenticatedOrReadOnly,)

    @staticmethod
    def get(request, pk):
        print('in detail')
        ad = Ad.objects.filter(pk=pk).annotate(
            user_max_bid=Max('bids__value', filter=Q(bids__bidder=request.user))).get()
        serializer = AdDetailSerializer(ad)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        ad = self.get_object(pk=pk)

        serializer = AdDetailSerializer(ad, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=request.user.pk)
            ad = self.get_object(pk=pk)
            if (user == ad.owner):
                ad.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class BidCreateView(APIView):
    def post(self, request, pk):
        serializer = BidSerializer(data={**request.data, 'bidder': request.user.id, 'ad': pk})
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
