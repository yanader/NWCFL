import bs4
import requests
import re


class FixturesParser:
    def __init__(self, date: str):
        self.__forthcoming_url = 'https://www.nwcfl.com/noformat-fixtures.php'
        self.__past_url = 'https://www.nwcfl.com/noformat-results.php'
        self.__date = date
        self.__games_dictionary = {}
        self.execute()

        #self.create_soup(self.__forthcoming_url)

    def execute(self):
        soup = self.create_soup(self.__forthcoming_url)
        soup_dates = soup.select('body > div > div > div > div > b')
        soup_games = soup.select('body > div > div > div > div > table')
        unformatted_dates_list = str(soup_dates).split(',')
        unformatted_games_list = str(soup_games).split(',')
        formatted_dates_list = self.clean_dates(unformatted_dates_list)
        formatted_games_list = self.clean_games(unformatted_games_list)


    def clean_dates(self, date_list: list):
        return_list = []
        removal_strings = [']', '[', '\t', '<br/>', '<br>', '</b>', '<b>', '\n', '  ']
        for date in date_list:
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
            for item in removal_strings:
                s = s.replace(item, '')
            s = s.replace('</tr>', '\n')
            s = s.replace('amp;', '')
            s = s.replace('-', ' - ')
            s = s.replace(' v ', ' - ')
            s = s.strip()
            s = s.split('\n')

            s = self.remove_score_from_results(s)
            return_list.append(s)
        return return_list

    def remove_score_from_results(games: list):
        return_list = []
        regex = re.compile(r'''
                    \d{1,2}
                    -
                    \d{1,2}
                    ''', re.VERBOSE)
        for game in games:
            return_list.append(re.sub(regex, ' - ', game))
        return return_list

    def create_soup(self, url: str):
        res_games = requests.get(url)
        res_games.raise_for_status()  # will kill the programme if the URL is 404
        soup = bs4.BeautifulSoup(res_games.text, 'html.parser')
        return soup






