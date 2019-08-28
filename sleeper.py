import os
import sleeper_wrapper

LEAGUE_ID = 433017068120436736

league = sleeper_wrapper.League(LEAGUE_ID)

users = league.get_users()

user_id_mapper = {}
name_user_mapper = {
    "arcorey15": "Alan Corey",
    "Dmandre161": "Derek Andre",
    "BauerS": "Bauer Schmeltz",
    "rileymprice": "Riley Price",
    "ergroff": "Ethan Groff",
    "ScottyJo24": "Scotty Johansen",
    "anddixon": "Andrew Dixon",
    "warrior80": "John Essex",
    "xbenld": "Ben",
    "rawrmirez": "Ramirez",
    "HappyGovtWorker": "Wes Brown",
    "cwiles32": "Chris Wiles",
}

for user in users:
    user_id_mapper[user["user_id"]] = user["display_name"]

