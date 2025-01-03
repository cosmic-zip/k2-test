from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from fakeapi.permissions import *
from fakeapi.serializers import CustomUserSerializer

class HealthyView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        data = {"status":"ok","message":"API is healthy"}
        return Response(data)

class UserView(APIView):
    permission_classes = [IsUser]

    def get(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)

class AdminView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)
