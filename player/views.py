from rest_framework import generics
from .models import Player
from .serializers import PlayerSerializer
from .permissions import IsAdminOrReadOnly
# Create your views here.

class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    #permission_classes = (IsAdminOrReadOnly,)

class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    #permission_classes = (IsAdminOrReadOnly,)