from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class TestView(APIView):

    def get(self, request):
        print(request)
        return Response({'Test': 'Seems fine "messages"'}, status=status.HTTP_200_OK)
