import bs4
import requests
import date_formatting as df


def clean_dates():
    pass

def upcoming_matches():
    pass

def past_matches():
    pass

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
    date_removal_strings = [']', '[', '\t', '<br/>', '<br>', '</b>', '<b>', '\n', '  ']
    games_removal_strings = ['[', '<tr>', '<td>', '</td>', '</b>', '<b>', '<table>', '</table>']

    date_list = str(soup_date).split(',')
    game_list = str(soup_games).split(',')

    for i in range(10):
        string_date = str(date_list[i])
        string_games = str(game_list[i])
        for item in date_removal_strings:
            string_date = string_date.replace('\n', ' - ')
            string_date = string_date.replace(item, '')
            string_date = string_date.strip()
        for item in games_removal_strings:
            string_games = string_games.replace(item, '')
            string_games = string_games.replace('</tr>', '\n')
            string_games = string_games.replace('amp;', '')
            string_games = string_games.strip()

        print(string_date)
        print(string_games)
        print()

    return matches_dictionary



matchDate = df.custom_date()
print(matchDate + ' - ')
gameday_dict = create_dictionary(matchDate, "fixtures")
print(gameday_dict)
