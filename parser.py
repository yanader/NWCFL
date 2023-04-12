import bs4
import requests
import re


class FixturesParser:
    def __init__(self, date: str):
        self.__forthcoming_url = 'https://www.nwcfl.com/noformat-fixtures.php'
        self.__past_url = 'https://www.nwcfl.com/noformat-results.php'
        self.__date = date
        self.__games_dictionary = {}
        self.__daily_team_list = []
        self.__postponed_list = []
        self.__teams_playing_list = []
        self.execute()


    def execute(self):
        self.__games_dictionary = self.create_forward_facing_dict()
        past_games_dict = self.create_backward_looking_dict()
        self.__games_dictionary.update(past_games_dict)
        self.remove_score_from_results(self.__games_dictionary)
        self.__postponed_list = self.create_postponed_list()
        self.__teams_playing_list = self.create_playing_list(self.__postponed_list)


    def get_teams_playing_list(self):
        return self.__teams_playing_list

    def get_postponed_list(self):
        return self.__postponed_list

    def get_game_dictionary(self):
        return self.__games_dictionary

    def create_twitter_dictionary(self):
        twitter_dict = {}
        team_file = open('T:\\Coding\\Projects\\Python\\NWCFL\\teamsDictionary.txt')
        teams = team_file.read()
        team_file.close()
        team_list = teams.split('\n')
        for team in team_list:
            team_items = team.split('-')
            if team_items[1] in self.__teams_playing_list:
                twitter_dict[team_items[1]] = team_items[0]
        return twitter_dict


    def create_playing_list(self, postponed_list: list):
        playing = []
        for key, value in self.__games_dictionary.items():
            for match in value:
                teams = match.split(' - ')
                playing.append(teams[0])
                playing.append(teams[1])
        for game in postponed_list:
            teams = game.split(' - ')
            playing.remove(teams[0])
            playing.remove(teams[1])
        return playing

    def create_postponed_list(self):
        postponed = []
        for key, value in self.__games_dictionary.items():
            new_value = []
            for match in value:
                new_match = match.replace('P - P', ' - ')
                if 'P - P' in match:
                    postponed.append(new_match)
                    new_value.append(new_match)
                else:
                    new_value.append(new_match)
            self.__games_dictionary[key] = new_value
        return postponed


    def create_forward_facing_dict(self):
        soup = self.create_soup(self.__forthcoming_url)
        soup_dates = soup.select('body > div > div > div > div > b')
        soup_games = soup.select('body > div > div > div > div > table')
        unformatted_dates_list = str(soup_dates).split(',')
        unformatted_games_list = str(soup_games).split(',')
        formatted_dates_list = self.clean_dates(unformatted_dates_list)
        formatted_games_list = self.clean_games(unformatted_games_list)
        return self.create_game_day_dictionary(formatted_dates_list, formatted_games_list)

    def create_backward_looking_dict(self):
        soup = self.create_soup(self.__past_url)
        soup_dates = soup.select('body > div > div > div > div > b')
        soup_games = soup.select('body > div > div > div > div > table')
        unformatted_dates_list = str(soup_dates).split(',')
        unformatted_games_list = str(soup_games).split(',')
        formatted_dates_list = self.clean_dates(unformatted_dates_list)
        formatted_games_list = self.clean_games(unformatted_games_list)
        return self.create_game_day_dictionary(formatted_dates_list, formatted_games_list)

    def create_game_day_dictionary(self, date_list: list, game_list: list):
        game_day_dict = {}
        for i in range(0, len(date_list) - 1):
            if self.__date in date_list[i] and 'Division' in date_list[i]:
                game_day_dict[date_list[i]] = game_list[i]
        return game_day_dict

    def clean_dates(self, date_list: list):
        return_list = []
        removal_strings = [']', '[', '\t', '<br/>', '<br>', '</b>', '<b>', '\n', '  ']
        for date in date_list:  # I want to write a function that does all this cleaning
            s = date
            s = s.replace('\n', ' - ')
            for item in removal_strings:
                s = s.replace(item, '')
            s = s.strip()
            return_list.append(s)
        return return_list

    def clean_games(self, game_list: list):
        return_list = []
        removal_strings = ['[', '<tr>', '<td>', '</td>', '</b>', '<b>', '<table>', '</table>',
                                 '<td width=\"45%\">', '<td width=\"10%\">']
        for date in game_list:
            s = date
            for item in removal_strings:  # I want to write a function that does all this cleaning
                s = s.replace(item, '')
            s = s.replace('</tr>', '\n')
            s = s.replace('amp;', '')
            s = s.replace('-', ' - ')
            s = s.replace(' v ', ' - ')
            s = s.strip()
            s = s.split('\n')

            return_list.append(s)
        return return_list

    def remove_score_from_results(self, games: dict):
        regex = re.compile(r'''
                    \d{1,2}
                    \s-\s
                    \d{1,2}
                    ''', re.VERBOSE)
        for key, batch in games.items():
            new_batch = []
            for s in batch:
                new_s = re.sub(regex, ' - ', s)
                new_batch.append(new_s)
            games[key] = new_batch


    def create_soup(self, url: str):
        res_games = requests.get(url)
        res_games.raise_for_status()  # will kill the programme if the URL is 404
        soup = bs4.BeautifulSoup(res_games.text, 'html.parser')
        return soup






