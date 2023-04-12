import date_formatting as df
from parser import FixturesParser
import twitter_reader2 as tr
from match import Match

custom_date = df.custom_date(1)
print(custom_date)

fp = FixturesParser(custom_date)

games_dictionary = fp.get_game_dictionary()
postponed_list = fp.get_postponed_list()
teams_playing_list = fp.get_teams_playing_list()
twitter_dict = fp.create_twitter_dictionary()

print(games_dictionary)
print(postponed_list)
print(teams_playing_list)
print(twitter_dict)
match_object_list = []

for key, item in games_dictionary.items():
    for game in item:
        teams = game.split(' - ')
        competition = key.split(' - ')[1]
        match_object_list.append(Match(teams[0], teams[1], competition))

for match in match_object_list:
    print(match)

tr.tweet_reader(twitter_dict)



