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
import re
from datetime import datetime

teams_file = 'teams.json'
players_file = 'players.json'
matches_file = 'matches.json'


class WorkJSON:
    def __init__(self):
        self.filename = 'default'
        self.data = {}

    def to_json(self):
        with open(self.filename, 'a') as file:
            data = json.dumps(self.data) + '\n'
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
        self.filename = teams_file
        self.data = {"team_id": self.team_id, "name": self.name}


class Player(WorkJSON):
    def __init__(self, player_id, name, team):
        WorkJSON.__init__(self)
        self.player_id = player_id
        self.name = name
        self.team = team
        self.filename = players_file
        self.data = {"player_id": self.player_id, "name": self.name, "team": self.team}


class Match:
    match_instances = []

    def __init__(self, team0, team1, match_id, date, location, result):
        self.__class__.match_instances.append(self)
        self.match_id = match_id
        self.date = date
        self.location = location
        self.result = result
        self.team0 = team0
        self.team1 = team1
        self.players = team0.players + team1.players

    def __str__(self):
        return 'Date: {}  Location: {}\n' \
               'Teams: {} vs {} Result: {}\n' \
               'Players: {}'.format(self.date, self.location, self.team0.name, self.team1.name, self.result,
                                    ', '.join([player.name for player in self.players]))


def existing_teams():
    with open(teams_file, 'r') as file:
        existing_teams_list = [json.loads(team_data) for team_data in file]
        return existing_teams_list


def add_players(existing_teams_):
    team_name = input('Enter player team:').strip()
    for team in existing_teams_:
        if team_name == team["name"]:
            team_id = team["team_id"]
            player_name = input('Enter player name:').strip()
            if re.match('^[A-Za-z -]*$', player_name):
                player_id = str(uuid.uuid4())[:4]
                new_player = Player(player_id, player_name, team_id)
                new_player.to_json()
                print('Successfully added new player: ', player_name, 'to team', team_name)
                return new_player
            else:
                print('Player was not added...\n Reason: wrong input...')
                return None
        else:
            continue
    print('Team does not exist. Exiting...')
    return None


def add_teams(existing_teams_):
    team_id = str(uuid.uuid4())[:4]
    name = input('Enter team name:').strip()
    if re.match('^[A-Za-z0-9_-]*$', name) and name not in [team["name"] for team in existing_teams_]:
        new_team = Team(team_id, name)
        new_team.to_json()
        print('Successfully added new team:\n', team_id, name)
        return new_team
    else:
        print('Team was not added...\n Reason: wrong input or team already exists...')
        return None


def add_matches(existing_teams_):
    team1_name = input('Enter the first team:').strip()
    team1_id = False
    team2_id = False
    for team1 in existing_teams_:
        if team1_name == team1["name"]:
            team1_id = team1["team_id"]

            team2_name = input('Enter the second team:').strip()
            for team2 in existing_teams_:
                if team2_name == team2["name"]:
                    team2_id = team2["team_id"]

    if team1_id and team2_id:
        date = input('Enter date (dd.mm.yyyy):').strip()
        try:
            datetime.strptime(date, '%d.%m.%Y')
            location = input('Enter location:').strip()
            if re.match('^[A-Za-z0-9_-]*$', location):
                result = input('Enter match result:').strip()
                if re.match('^[0-9:]*$', result):
                    match_id = str(uuid.uuid4())[:4]
                    new_match = {"team0": team1_id, "team1": team2_id, "match_id": match_id, "date": date,
                                 "location": location, "result": result}
                    with open(matches_file, 'a') as file:
                        data = json.dumps(new_match) + '\n'
                        file.write(data)

                    return new_match

                else:
                    print('Wrong value for result..')
            else:
                print('Wrong value for location...')

        except Exception as date_error:
            print('Wrong input', date_error)

    else:
        print('Team does not exist. Exiting...')
        return None


def add_data():
    data_to_add_choice = input('What would you like to add:\n'
                               '1 - Team\n'
                               '2 - Player\n'
                               '3 - Match\n')
    if data_to_add_choice in ('1', '2', '3'):

        existing_teams_list = existing_teams()

        if data_to_add_choice == '1':
            print('Let\'s add a team...')
            add_teams(existing_teams_list)

        elif data_to_add_choice == '2':
            print('Let\'s add a player...')
            add_players(existing_teams_list)

        elif data_to_add_choice == '3':
            print('Let\'s add a match...')
            add_matches(existing_teams_list)

    else:
        print('Wrong choice to add!')


def init_instances():
    teams_list = []
    with open(teams_file, 'r') as teams_:
        for line in teams_:
            team_data = json.loads(line)

            teams_list.append(Team(team_data["team_id"], team_data["name"]))

    players_list = []
    created_teams_ids = [inst.team_id for inst in teams_list]

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

    matches_list = []

    with open(matches_file, 'r') as matches_:
        for line in matches_:
            match = json.loads(line)
            match_teams = [teams_list[created_teams_ids.index(team_id)]
                           for team_id in [match.pop(team_id) for team_id in ('team0', 'team1')]]
            matches_list.append(Match(*match_teams, **match))
    return matches_list


def search(matches):
    match_dates = [match.date for match in matches]

    search_dates = input('Enter criteria: date or period').strip().split()
    try:
        if len(search_dates) == 1:
            date = datetime.strptime(search_dates[0], '%d.%m.%Y')
            for i, match_date in enumerate(match_dates):
                if datetime.strptime(match_date, '%d.%m.%Y') == date:
                    print('\n', matches[i], '\n')

        elif len(search_dates) == 2:
            date0, date1 = datetime.strptime(search_dates[0], '%d.%m.%Y'), \
                           datetime.strptime(search_dates[1], '%d.%m.%Y')
            if date0 > date1:
                print("Wrong period - last date is earlier than the first one...")
            else:
                for i, match_date in enumerate(match_dates):
                    if date0 <= datetime.strptime(match_date, '%d.%m.%Y') <= date1:
                        print('\n', matches[i], '\n')
        else:
            print('Wrong input...')

    except Exception as date_error:
        print('Wrong input', date_error)


def main():
    while True:

        user_choice = input('What would you like to do?\n'
                            '1 - Add data (Team, Player, Match)\n'
                            '2 - Search matches\n'
                            '3 - Exit\n')

        if user_choice in ('1', '2', '3'):

            if user_choice == '1':
                add_data()

            elif user_choice == '2':
                match_instances_list = init_instances()
                search(match_instances_list)

            elif user_choice == '3':
                print('Exiting...')
                break

        else:
            print('Wrong choice!')


if __name__ == '__main__':
    main()
