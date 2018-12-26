#from rest_framework.decorators import api_view

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



"""
FUNCTION_BASED VIEWS

@api_view(['GET', 'POST'])
def teamList(request):
    if request.method == 'GET':
        queryset = Team.objects.all()
        serializer = TeamSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view()
def teamDetail(request, pk):
    if request.method == 'GET':
        queryset = Team.objects.get(pk=pk)
        serializer = TeamSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
"""