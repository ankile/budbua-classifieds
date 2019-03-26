from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Rating

# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import RatingSerializer


class RatingView(APIView):
    def post(self, request):
        serializer = RatingSerializer(data={
            'rating':request.data.get('rating'),
            'rating_giver': request.user.id,
            'rating_receiver': request.GET.get('ratingReceiver'),
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request):
        rating = Rating.objects.get(rating_receiver=request.GET.get('ratingReceiver'), rating_giver=request.user.id)
        serializer = RatingSerializer(rating, data={**request.data, 'rating_giver': request.user.id}, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    def get(self, request):
        rating = Rating.objects.filter(rating_receiver=request.GET.get('ratingReceiver'), rating_giver=request.user.id)
        if rating.exists():
            serializer = RatingSerializer(rating.get())
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)
