# -*- coding: utf-8 -*-
import logging
from functools import partial
import json
import os

from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView, exception_handler
from app.models import Player, PlayerStats, Shot, Game, Team
from django.core.exceptions import ObjectDoesNotExist


LOGGER = logging.getLogger('django')


# define how data is processed and what is returned.
# The views interact with the models to fetch data from the database and return it to the client
class PlayerSummary(APIView):
    logger = LOGGER

    def __init__(self):
        super().__init__()


    def get(self, request, playerID):
        """Return player data"""
        try:
            player = Player.objects.get(id=playerID)
        except Player.DoesNotExist:
            raise Http404("Player does not exist.")

        games_data = []
        for stat in player.statistics.all():
            shots_data = [
                {
                    "isMake": shot.is_make,
                    "locationX": shot.location_x,
                    "locationY": shot.location_y,
                }
                for shot in stat.shots.all()
            ]

            game_data = {
                "team": stat.team.name,
                "id": stat.game.id,
                "date": stat.game.game_date,
                "isStarter": stat.is_starter,
                "minutes": stat.minutes,
                "points": stat.points,
                "assists": stat.assists,
                "offensiveRebounds": stat.offensive_rebounds,
                "defensiveRebounds": stat.defensive_rebounds,
                "steals": stat.steals,
                "blocks": stat.blocks,
                "turnovers": stat.turnovers,
                "defensiveFouls": stat.defensive_fouls,
                "offensiveFouls": stat.offensive_fouls,
                "freeThrowsMade": stat.free_throws_made,
                "freeThrowsAttempted": stat.free_throws_attempted,
                "twoPointersMade": stat.two_pointers_made,
                "twoPointersAttempted": stat.two_pointers_attempted,
                "threePointersMade": stat.three_pointers_made,
                "threePointersAttempted": stat.three_pointers_attempted,
                "shots": shots_data,
            }
            games_data.append(game_data)

        data = {
            'id': player.id,
            "name": player.name,
            "games": games_data
        }


        # TODO: Complete API response, replace placeholder below with actual implementation that sources data from database
        # print(os.path.dirname(os.path.abspath(__file__)))
        # with open(os.path.dirname(os.path.abspath(__file__)) + '/sample_response/sample_response.json') as sample_response:
        #     data = json.load(sample_response)
        return Response(data)
