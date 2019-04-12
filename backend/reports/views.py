from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import AdReportSerializer, UserReportSerializer


# Create your views here.
class AdReportCreateView(APIView):
    def post(self, request, pk):
        serializer = AdReportSerializer(data={**request.data, 'reporter': request.user.id, 'ad': pk})
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserReportCreateView(APIView):
    def post(self, request, pk):
        serializer = UserReportSerializer(data={**request.data, 'reporter': request.user.id, 'reported': pk})
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
