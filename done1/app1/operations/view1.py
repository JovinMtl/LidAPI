from django.contrib.auth.models import User
from ..serializers import UserSeriazer
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, \
    IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser


class UserMan(generics.ListAPIView):
    """I want to view and add user"""
    queryset = User.objects.all()
    serializer_class = UserSeriazer
    permission_classes = [IsAuthenticated]

class UserViewSet(viewsets.ViewSet):
    """I want to list and retrieves all my users"""

    def list(self, request):
        queryset = User.objects.all()
        serializer_class = UserSeriazer(queryset, many=True)
        return Response(serializer_class.data)
