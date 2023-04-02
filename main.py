import date_formatting as df
import parser as p
import twitter_reader as tr


# Monday 27th March 2023
matchDate = df.custom_date()
print(matchDate + '\n')

fixture_dict = p.create_fixture_dict(matchDate)
result_dict = p.create_results_dict(matchDate)

play_today_list = p.create_team_list(fixture_dict, result_dict)


if len(play_today_list) == 0:
    print("There are no matches today.")
else:
    tr.tweet_reader(play_today_list)
