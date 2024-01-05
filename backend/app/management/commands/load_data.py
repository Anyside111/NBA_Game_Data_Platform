import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from app.models import Player, PlayerStats, Shot, Game, Team


# Function to load the data
def load_data():
    # Load teams
    with open(
            'D:\\github_projects\\Anyside111\\technical-project-deadline-09-08-23-Anyside111\\backend\\raw_data\\teams.json',
            'r') as file:
        teams_data = json.load(file)
        for team_data in teams_data:
            team, created = Team.objects.get_or_create(id=team_data['id'], defaults={'name': team_data['name']})
            if not created and team.name != team_data['name']:
                team.name = team_data['name']
                team.save()

    # Load players
    with open(
            'D:\\github_projects\\Anyside111\\technical-project-deadline-09-08-23-Anyside111\\backend\\raw_data\\players.json',
            'r') as file:
        players_data = json.load(file)
        for player_data in players_data:
            player, created = Player.objects.get_or_create(id=player_data['id'], defaults={'name': player_data['name']})
            if not created and player.name != player_data['name']:
                player.name = player_data['name']
                player.save()

    # Load games and player stats
    with open('D:\\github_projects\\Anyside111\\technical-project-deadline-09-08-23-Anyside111\\backend\\raw_data\\games.json', 'r') as file:
        games_data = json.load(file)
        for game_data in games_data:
            home_team = Team.objects.get(id=game_data["homeTeam"]["id"])
            away_team = Team.objects.get(id=game_data["awayTeam"]["id"])
            game, created = Game.objects.get_or_create(id=game_data["id"], game_date=game_data["date"], home_team=home_team, away_team=away_team)

            for team_data in [game_data["homeTeam"], game_data["awayTeam"]]:
                current_team = home_team if team_data == game_data["homeTeam"] else away_team
                for player_data in team_data['players']:
                    player = Player.objects.get(id=player_data['id'])
                    defaults = {
                        'team': current_team,
                        'is_starter': player_data['isStarter'],
                        'minutes': player_data['minutes'],
                        'points': player_data['points'],
                        'assists': player_data['assists'],
                        'offensive_rebounds': player_data['offensiveRebounds'],
                        'defensive_rebounds': player_data['defensiveRebounds'],
                        'steals': player_data['steals'],
                        'blocks': player_data['blocks'],
                        'turnovers': player_data['turnovers'],
                        'defensive_fouls': player_data['defensiveFouls'],
                        'offensive_fouls': player_data['offensiveFouls'],
                        'free_throws_made': player_data['freeThrowsMade'],
                        'free_throws_attempted': player_data['freeThrowsAttempted'],
                        'two_pointers_made': player_data['twoPointersMade'],
                        'two_pointers_attempted': player_data['twoPointersAttempted'],
                        'three_pointers_made': player_data['threePointersMade'],
                        'three_pointers_attempted': player_data['threePointersAttempted'],
                    }
                    player_stats, created = PlayerStats.objects.get_or_create(player=player, game=game, defaults=defaults)

                    # Update stats if record already exists and new data is different
                    if not created:
                        for key, value in defaults.items():
                            if getattr(player_stats, key) != value:
                                setattr(player_stats, key, value)
                        player_stats.save()  # Save the updated record

                    for shot_data in player_data['shots']:
                        defaults = {
                            'is_make': shot_data['isMake'],
                            'location_x': shot_data['locationX'],
                            'location_y': shot_data['locationY'],
                        }
                        shot, created = Shot.objects.get_or_create(player_statistic=player_stats, **defaults)
                        if not created:
                            for key, value in defaults.items():
                                if getattr(shot, key) != value:
                                    setattr(shot, key, value)
                            shot.save()


if __name__ == "__main__":
    # This ensures the script runs only if executed directly, not if imported elsewhere
    # Load the data
    load_data()
