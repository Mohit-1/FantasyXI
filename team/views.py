from .models import Team, TeamPlayerRelation
from .serializers import TeamSerializer, TeamPlayerRelationSerializer
from rest_framework import generics
from .permissions import IsOwnerOrAdmin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamDetail(APIView):       
    def get(self, request):
        pass

    def post(self, request):
        pass
    
    def delete(self, request):
        pass


class TeamPlayerUpdate(APIView):
    def post(self, request):
        serializer = TeamPlayerRelationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

    def delete(self, request):    
        serializer = TeamPlayerRelationSerializer(data=request.data)
        if serializer.is_valid():
            team = serializer.data.get('team')
            player = serializer.data.get('player')
            relation = TeamPlayerRelation.objects.filter(team=team, player=player)
            relation.delete()

            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        
