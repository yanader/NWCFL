import bs4
import requests
import re


def create_dictionary(date_string: str, url: str):
    if url == 'fixtures':
        res_games = requests.get('https://www.nwcfl.com/noformat-fixtures.php')
    elif url == 'results':
        res_games = requests.get('https://www.nwcfl.com/noformat-results.php')
    res_games.raise_for_status()
    soup = bs4.BeautifulSoup(res_games.text, 'html.parser')

    soup_date = soup.select('body > div > div > div > div > b')
    soup_games = soup.select('body > div > div > div > div > table')

    matches_dictionary = {}

    date_list_input = str(soup_date).split(',')
    game_list_input = str(soup_games).split(',')

    date_list = clean_dates(date_list_input)
    game_list = clean_games(game_list_input)

    for i in range(0, len(date_list) - 1):
        if date_string in date_list[i]:
            matches_dictionary[date_list[i]] = game_list[i]

    return matches_dictionary


def clean_dates(date_list:list):
    return_list = []
    date_removal_strings = [']', '[', '\t', '<br/>', '<br>', '</b>', '<b>', '\n', '  ']
    for date in date_list:
        s = date
        s = s.replace('\n', ' - ')
        for item in date_removal_strings:
            s = s.replace(item, '')
        s = s.strip()
        return_list.append(s)
    return return_list


def clean_games(game_list:list):
    return_list = []
    games_removal_strings = ['[', '<tr>', '<td>', '</td>', '</b>', '<b>', '<table>', '</table>', '<td width=\"45%\">','<td width=\"10%\">']
    for date in game_list:
        s = date
        for item in games_removal_strings:
            s = s.replace(item, '')
        s = s.replace('</tr>', '\n')
        s = s.replace('amp;', '')
        s = s.replace('-', ' - ')
        s = s.replace(' v ', ' - ')
        s = s.strip()
        s = s.split('\n')

        s = remove_score_from_results(s)
        return_list.append(s)
    return return_list


def remove_score_from_results(games:list):
    return_list = []
    regex = re.compile(r'''
                \d{1,2}
                -
                \d{1,2}
                ''', re.VERBOSE)
    for game in games:
        return_list.append(re.sub(regex, ' - ', game))
    return return_list


def playing_today(game_day_dict: dict) ->list:
    team_names_playing_today = []
    for key, values in game_day_dict.items():
        for value in values:
            if 'P-P' in value:
                continue
            if '-' in value:
                teams = value.strip().split('-')
            else:
                teams = value.split(' v ')
            if teams[0] not in team_names_playing_today:
                team_names_playing_today.append(teams[0].strip())
            if teams[1] not in team_names_playing_today:
                team_names_playing_today.append(teams[1].strip())
    return team_names_playing_today


def daily_twitter_dictionary(teams_playing_today: list) ->dict:
    team_file = open('T:\\Coding\\Projects\\Python\\NWCFL\\teamsDictionary.txt')
    teams = team_file.read()
    team_file.close()

    team_list = teams.split('\n')
    team_dictionary = {}
    for team in team_list:
        team_items = team.split('-')
        if team_items[1] in teams_playing_today:
            team_dictionary[team_items[1]] = team_items[0]
    return team_dictionary


def dictionary_processor(gameday:dict):
    daily_fixtures_list = []
    for k, v in gameday.items():
        for match in v:
            teams = match.split(' - ')
            daily_fixtures_list.append([k, teams[0].strip(), teams[1].strip(), ['0-0']])
    return daily_fixtures_list

def formatted_list(gameday: dict):
    formatted_return_list = []
    for k, v in gameday.items():
        for match in v:
            teams = match.strip().split('-')
            formatted_return_list.append([teams[0].strip(), '0-0', teams[1].strip()])
    return formatted_return_list








