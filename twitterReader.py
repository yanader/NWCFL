import snscrape.modules.twitter as sntwitter
import re, os

def tweet_reader(playing_today: list):
    teamFile = open('T:\\Coding\\NWCFL\\teamsDictionary.txt')
    teams = teamFile.read()
    teamFile.close()
    teamList = teams.split('\n')
    teamDictionary = {}
    for team in teamList:
        teamItems = team.split('-')
        if teamItems[1] in playing_today:
            teamDictionary[teamItems[0]] = teamItems[1]

# Created a list to append all tweet attributes(data)
    attributes_container = []
    scoreRegex = re.compile(r'''
            #[^:\n]
            \d{1,2}
            -
            \d{1,2}
            #[^:!.]
            ''', re.VERBOSE)

# Using TwitterSearchScraper to scrape data and append tweets to list
    for team in teamDictionary.keys():
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper('from:'+team).get_items()):
            if i > 5:
                break
            text = tweet.rawContent
            extract = scoreRegex.findall(text)
            if len(extract) > 0:
                extract_string = extract[0]
                extract_string = extract_string.replace('\n', '')
                extract_string = extract_string.replace(' ', '')
                attributes_container.append([tweet.user.username, extract_string])

    for tweet in attributes_container:
        print(tweet[0] + ' ' + tweet[1])

