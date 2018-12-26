from django.db import models

# Create your models here.
class Player(models.Model):
    POSITIONS = (('GK', 'Goalkeeper'), ('DEF', 'Defender'), ('MID', 'Midfielder'), ('FW', 'Forward'))

    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    jersey_number = models.CharField(max_length=2)
    position = models.CharField(choices=POSITIONS, max_length=5)
    valuation = models.FloatField()
    #role = models.CharField()

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'

    def __str__(self):
        return self.first_name + " " + self.last_name
