import snscrape.modules.twitter as sntwitter
import re


def tweet_reader(playing_today: list):
    team_file = open('T:\\Coding\\Projects\\Python\\NWCFL\\teamsDictionary.txt')
    teams = team_file.read()
    team_file.close()
    team_list = teams.split('\n')
    team_dictionary = {}
    for team in team_list:
        team_items = team.split('-')
        if team_items[1] in playing_today:
            team_dictionary[team_items[0]] = team_items[1]

# Created a list to append all tweet attributes(data)
    attributes_container = []
    score_regex = re.compile(r'''
            #[^:\n]
            \d{1,2}
            -
            \d{1,2}
            #[^:!.]
            ''', re.VERBOSE)

# Using TwitterSearchScraper to scrape data and append tweets to list
    for team in team_dictionary.keys():
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper('from:'+team).get_items()):
            if i > 1:
                break
            text = tweet.rawContent
            extract = score_regex.findall(text)
            if len(extract) > 0:
                extract_string = extract[0]
                extract_string = extract_string.replace('\n', '')
                extract_string = extract_string.replace(' ', '')
                attributes_container.append([tweet.user.username, extract_string])

    for tweet in attributes_container:
        print(tweet[0] + ' ' + tweet[1])

