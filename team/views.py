from .models import Team, TeamPlayerRelation
from .serializers import TeamSerializer, TeamPlayerRelationSerializer
from player.serializers import PlayerSerializer
from player.models import Player
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from permissions import IsTeamOwner
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ListCreateTeam(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    #permission_classes = (IsAuthenticated, )

class TeamDetail(generics.RetrieveAPIView):       
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    #permission_classes = (IsAuthenticated, )

class EditTeam(APIView):
    def put(self, request, pk):
        try:
            team = Team.objects.get(pk=pk)
        except Team.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        name = request.data.get('name')
        team.name = name
        team.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

class LineUp(APIView):
    def get(self, request, pk):
        try:
            team = Team.objects.get(pk=pk)
        except Team.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        queryset = TeamPlayerRelation.objects.filter(team=team)
        player_list = []

        for relation in queryset:
            player_list.append(relation.player)

        serializer = PlayerSerializer(player_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AddPlayerToTeam(APIView):
    def post(self, request):
        serializer = TeamPlayerRelationSerializer(data=request.data)
        if serializer.is_valid():
            team = serializer.validated_data.get('team')
            player = serializer.validated_data.get('player')

            # team = Team.objects.get(pk=team_pk)
            # player = Player.objects.get(pk=player_pk)

            if (team.budget_available >= player.valuation) and team.spots_available > 0:
                serializer.save()
                team.spots_available -= 1
                team.budget_available -= player.valuation
                team.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)

            else:
                return Response({"message" : "Player can not be added"})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class RemovePlayerFromTeam(APIView):
    def post(self, request):
        serializer = TeamPlayerRelationSerializer(data=request.data)
        if serializer.is_valid():
            team = serializer.validated_data.get('team')
            player = serializer.validated_data.get('player')

            TeamPlayerRelation.objects.filter(team=team, player=player).delete()
            team.spots_available += 1
            team.budget_available += player.valuation
            team.save()
            
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        