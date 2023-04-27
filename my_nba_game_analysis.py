import csv

import re

def loading_data(file):
    data = []

    with open(file, 'r') as fd:
        reader = csv.reader(fd, delimiter = '|')
        fields = next(reader)

        for row in reader:
            data.append(row)

    return data

def team_recognition(team1, team2):
    return team1 == team2

def analyse_nba_game(game_data):
    result = {"home_team": {"name": "", "players_data": {}}, "away_team": {"name": "Otherteam", "players_data": {}}}

    for move in game_data:
        current_team = move[2]
        home_team = move[3]
        away_team = move[4]
        current_act = move[7]

        three_pts_regexp = re.compile(r'(.*) makes 3-pt jump shot from')
        match = three_pts_regexp.search(current_act)

        if match is None:
            continue
        player_name = match[1]

        if team_recognition(away_team, current_team):
            if player_name not in result["away_team"]["players_data"]:
                result["away_team"]["players_data"][player_name] = {"3P": 0}
            result["away_team"]["players_data"][player_name]['3P'] += 1
        else:
            if player_name not in result["home_team"]["players_data"]:
                result["home_team"]["players_data"][player_name] = {"3P": 0}
            result["home_team"]["players_data"][player_name]['3P'] += 1
        
    return result

def start():

    game_data = loading_data("data_lights.txt")
    result = analyse_nba_game(game_data)
    print(result)

start()
