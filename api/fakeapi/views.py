from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import *

class HealthyView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        data = {"status":"ok","message":"API is healthy"}
        return Response(data)
