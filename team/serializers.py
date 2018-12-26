from rest_framework import serializers
from .models import Team, TeamPlayerRelation

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class TeamPlayerRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamPlayerRelation
        fields = '__all__'