# Задача 0
# Реализовать систему хранения информации о футбольном чемпионате.
# Информация опирается на следующие основные классы: Team (команда), Player (игрок), Match (матч).
# Эти классы связаны друг с другом посредством ассоциации.
#
# Атрибуты классов
#
# Team
#
# id — уникальный численный идентификатор.
# name — имя.
# players — игроки, играющие за данную команду в рамках чемпионата.
#
# Player
#
# id — уникальный численный идентификатор.
# name — имя
# team – команда.
#
# Match
#
# id — уникальный численный идентификатор.
# date — дата.
# location — место.
# result — счёт.
# team1 — первая команда.
# team2 — вторая команда.
# players – игроки, участвовавшие в матче.
#
# Реализовать возможность сохранения записей в файл,
# а также возможность поиска информации о матчах в указанные даты
# (предусмотреть возможность поиска по временному периоду)
# с выводом информации по командам и игрокам, участвовавшим в матчах.

import json
import uuid


class WorkJSON:
    def __init__(self):
        self.filename = 'default'
        self.data = {}

    def to_json(self):
        with open(self.filename, 'a') as file:
            data = json.dumps(self.data) + '\n'
            print(data)
            file.write(data)

    def from_json(self):
        with open(self.filename, 'r') as file:
            for data in file:
                yield json.loads(data)


class Team(WorkJSON):

    def __init__(self, team_id, name):
        WorkJSON.__init__(self)
        self.team_id = team_id
        self.name = name
        self.players = []
        self.filename = '/home/slava/dev/Temp/H13_Task00/teams.json'
        self.data = {"team_id": self.team_id, "name": self.name}


class Player(WorkJSON):
    def __init__(self, player_id, name, team):
        WorkJSON.__init__(self)
        self.player_id = player_id
        self.name = name
        self.team = team
        self.filename = '/home/slava/dev/Temp/H13_Task00/players.json'
        self.data = {"player_id": self.player_id, "name": self.name, "team": self.team}


class Match(WorkJSON):

    def __init__(self, match_id, date, location, result, team1, team2):
        WorkJSON.__init__(self)
        self.match_id = match_id
        self.date = date
        self.location = location
        self.result = result
        self.team1 = team1
        self.team2 = team2
        self.players = team1.players + team2.players
        self.filename = '/home/slava/dev/Temp/H13_Task00/matches.json'


def add_players():
    player_id = str(uuid.uuid4())[:4]
    name = input('Enter player name:').strip()
    team = input('Enter player team_id:').strip()

    new_player = Player(player_id, name, team)
    new_player.to_json()
    return new_player


def add_teams():
    team_id = str(uuid.uuid4())[:4]
    name = input('Enter team name:').strip()

    new_team = Team(team_id, name)
    new_team.to_json()
    return new_team


def add_matches():
    match_id = str(uuid.uuid4())[:4]
    date = input('Enter date (dd.mm.yyyy):').strip()
    location = input('Enter location:').strip()
    result = input('Enter match result:').strip()
    team1 = input('Enter the first team:').strip()
    team2 = input('Enter the second team:').strip()

    new_match = Match(match_id, date, location, result, team1, team2)
    return new_match


def init_instances():
    teams_file = '/home/slava/dev/Temp/H13_Task00/teams.json'
    players_file = '/home/slava/dev/Temp/H13_Task00/players.json'
    matches_file = '/home/slava/dev/Temp/H13_Task00/matches.json'
    teams_list = []
    with open(teams_file, 'r') as teams_:
        for line in teams_:
            team_data = json.loads(line)
            print(team_data)
            teams_list.append(Team(team_data["team_id"], team_data["name"]))
    print(teams_list)
    players_list = []
    created_teams_ids = [inst.name for inst in teams_list]
    print(created_teams_ids)
    with open(players_file, 'r') as players_:
        for line in players_:
            player_data = json.loads(line)
            player_team = teams_list[created_teams_ids.index(player_data.pop("team"))]
            players_list.append(
                Player(player_data["player_id"], player_data["name"], player_team))

    for team in teams_list:
        for player in players_list:
            if team is player.team:
                team.players.append(player)
                print(team.name, player.name)

    matches_list = []
    # with open


  def main():

    while True:
        add_matches()



if __name__ == '__main__':
    main()
