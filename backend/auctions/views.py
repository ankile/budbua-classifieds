from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from auctions.models import Ad
from auctions.serializers import AdCreateSerializer, AdListSerializer, AdDetailSerializer
from budbua.utils.mixins import ModelView


class AdsListCreateView(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly, )

    # TODO Implement searching and pagination
    @staticmethod
    def get(request):

        print(request.GET)
        search_query = request.GET.get("search","")
        ads = Ad.objects.filter(title__icontains=search_query)
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
    permission_classes = (IsAuthenticatedOrReadOnly, )

    @staticmethod
    def get(_, pk):
        ad = Ad.objects.get(pk=pk)
        serializer = AdDetailSerializer(ad)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        ad = self.get_object(pk=pk)

        serializer = AdDetailSerializer(ad, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_200_OK)

    def delete(self, _, pk):
        ad = self.get_object(pk=pk)
        ad.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
