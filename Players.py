import os
from sleeper_wrapper import Players

players = Players.get_all_players()
trending_players = Players

for player_id,player_info in players.items():
    