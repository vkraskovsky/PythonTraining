from django.db import models


# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=30)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Match(models.Model):
    teams = models.ManyToManyField(Team)
    location = models.CharField(max_length=20)
    score = models.CharField(max_length=5)

    def __str__(self):
        return self.location + ' ' + self.score
