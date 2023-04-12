import date_formatting as df
from parser import FixturesParser
import twitter_reader2 as tr


custom_date = df.custom_date(0)
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

tr.tweet_reader(twitter_dict)



