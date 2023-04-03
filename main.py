import date_formatting as df
import parser as p
import twitter_reader as tr


# Monday 27th March 2023
matchDate = df.custom_date()
print(matchDate + '\n')

gameday_dict = p.create_dictionary(matchDate, "fixtures")
gameday_dict.update(p.create_dictionary(matchDate, "results"))

print(gameday_dict)

today_team_list = p.playing_today(gameday_dict)

for team in today_team_list:
    print(team)
print()

if len(today_team_list) == 0:
    print("There are no matches today.")
else:
    tr.tweet_reader(today_team_list)
