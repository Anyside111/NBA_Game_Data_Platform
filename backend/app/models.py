# -*- coding: utf-8 -*-
from django.db import models


# defines the structure of the database tables.
# Each class in models.py corresponds to a table in the database.
class Team(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name

class Player(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Game(models.Model):
    id = models.IntegerField(primary_key=True)
    game_date = models.DateField()
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_games')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_games')

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} on {self.game_date}"

class PlayerStats(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='statistics')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='player_statistics')# linked to one game
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    is_starter = models.BooleanField()
    minutes = models.PositiveIntegerField()
    points = models.PositiveIntegerField()
    assists = models.PositiveIntegerField()
    offensive_rebounds = models.PositiveIntegerField()
    defensive_rebounds = models.PositiveIntegerField()
    steals = models.PositiveIntegerField()
    blocks = models.PositiveIntegerField()
    turnovers = models.PositiveIntegerField()
    defensive_fouls = models.PositiveIntegerField()
    offensive_fouls = models.PositiveIntegerField()
    free_throws_made = models.PositiveIntegerField()
    free_throws_attempted = models.PositiveIntegerField()
    two_pointers_made = models.PositiveIntegerField()
    two_pointers_attempted = models.PositiveIntegerField()
    three_pointers_made = models.PositiveIntegerField()
    three_pointers_attempted = models.PositiveIntegerField()

    def __str__(self):
        return f"Stats for {self.player.name} in {self.game}"

class Shot(models.Model):
    player_statistic = models.ForeignKey(PlayerStats, on_delete=models.CASCADE, related_name='shots')
    is_make = models.BooleanField()
    location_x = models.FloatField()
    location_y = models.FloatField()

    def __str__(self):
        return f"Shot by {self.player_statistic.player.name} in {self.player_statistic.game}"