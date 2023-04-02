import bs4
import requests


def create_fixture_dict(date_string: str):
    res_fixtures = requests.get('https://www.nwcfl.com/noformat-fixtures.php')
    res_fixtures.raise_for_status()
    soup_fixtures = bs4.BeautifulSoup(res_fixtures.text, 'html.parser')

    soup_date = soup_fixtures.select('body > div > div > div > div > b')
    soup_fixtures = soup_fixtures.select('body > div > div > div > div > table')

    fixtures_dictionary = {}
    date_removal_strings = ['\t', '<br/>', '<br>', '</b>', '<b>', '\n', '   ']
    fixture_removal_strings = ['<tr>', '<td>', '</td>', '</b>', '<b>', '<table>', '</table>']

    for i in range(5):
        s = str(soup_date[i])
        for item in date_removal_strings:
            s = s.replace(item, '')
        if date_string not in s:
            break
        s = s.replace(date_string + '  ', '')
        fixtures = str(soup_fixtures[i])
        fixtures = fixtures.replace('</td></tr>', '\n')
        for item in fixture_removal_strings:
            fixtures = fixtures.replace(item, '')
        fixtures = fixtures.replace('West Didsbury &amp; Chorlton','West Didsbury & Chorlton')
        daily_fixtures = fixtures.split('\n')
        daily_fixtures.pop()
        fixtures_dictionary[s] = daily_fixtures

    return fixtures_dictionary


def create_results_dict(date_string: str):
    res_results = requests.get('https://www.nwcfl.com/noformat-results.php')
    res_results.raise_for_status()
    soup_results = bs4.BeautifulSoup(res_results.text, 'html.parser')

    soup_date = soup_results.select('body > div > div > div > div > b')
    soup_results = soup_results.select('body > div > div > div > div > table')

    results_dictionary = {}
    date_removal_strings = ['\t', '<br/>', '<br>', '</b>', '<b>', '\n', '   ']
    results_removal_strings = ['<tr>', '<td>', '</td>', '</b>', '<b>', '<table>', '</table>']

    for i in range(5):
        s = str(soup_date[i])
        for item in date_removal_strings:
            s = s.replace(item, '')
        if date_string not in s:
            break
        s = s.replace(date_string + '  ', '')
        results = str(soup_results[i])
        results = results.replace('</td></tr>', '\n')
        for item in results_removal_strings:
            results = results.replace(item, '')
        results = results.replace('West Didsbury &amp; Chorlton','West Didsbury & Chorlton')
        daily_results = results.split('\n')
        daily_results.pop()
        new_daily_results = []
        for item in daily_results:
            new_string = item.replace('<td width="45%">', '')
            new_string = new_string.replace('<td width="10%">', '')
            new_daily_results.append(new_string)
        results_dictionary[s] = new_daily_results

    return results_dictionary


def create_team_list(fixture_dict: dict, results_dict: dict):
    playing_today = []
    for key, values in fixture_dict.items():
        for value in values:
            if 'P-P' in value:
                continue
            if '-' in value:
                teams = value.split('-')
            else:
                teams = value.split(' v ')
            if teams[0] not in playing_today:
                playing_today.append(teams[0])
            if teams[1] not in playing_today:
                playing_today.append(teams[1])

    for key, values in results_dict.items():
        for value in values:
            if 'P-P' in value:
                continue
            if '-' in value:
                teams = value.split('-')
            else:
                teams = value.split(' v ')
            if teams[0] not in playing_today:
                playing_today.append(teams[0])
            if teams[1] not in playing_today:
                playing_today.append(teams[1])

    return playing_today




