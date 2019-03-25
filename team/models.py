from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    budget_available = models.FloatField(editable=False, default=100.0)
    captain = models.ForeignKey('player.Player', editable=False, null=True, on_delete=models.SET_NULL)
    spots_available = models.IntegerField(editable=False, default=5)

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        return self.name

class TeamPlayerRelation(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player = models.ForeignKey('player.Player', on_delete=models.CASCADE)

    def __str__(self):
        return self.team.name + "-" +self.player.first_name


