from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import RatingSerializer


class TestView(APIView):

    def get(self, request):
        print(request)
        return Response({'Test': 'this works "rating"'}, status=status.HTTP_200_OK)


class RatingCreateView(APIView):
    def post(self, request):
        serializer = RatingSerializer(data={**request.data, 'rating_giver':request.user.id})
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        return Respons(serializer.data, status=status.HTTP_201_CREATED)
