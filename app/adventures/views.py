from django.shortcuts import render
from rest_framework import permissions, viewsets

from app.adventures.serializers import (
    AdventureSerializer,
    UserSerializer,
    EventSerializer,
)
from app.adventures.models import Adventure, Event, User


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewd or edited
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class AdventureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows adventures to be viewd or edited
    """
    
    serializer_class = AdventureSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Adventure.objects.filter(user_id=self.request.user).order_by("name")
    


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows events to be viewd or edited
    """

    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Event.objects.filter(adventure_id=self.request.query_params["adventure"]).order_by("name")
    
