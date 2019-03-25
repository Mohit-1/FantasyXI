from rest_framework import generics
from .models import Player
from .serializers import PlayerSerializer

class ListCreatePlayer(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class EditPlayer(generics.UpdateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer