import dateFormatting as dF
import parser as p
import twitterReader as tr
# 1) load fixtures for the day
# 2) produce list of teams (from txt file) who have mathces today
# 3) load tweets for those teams only

# Monday 27th March 2023
matchDate = dF.custom_date()

print(matchDate + '\n')
fixture_dict = p.create_fixture_dict(matchDate)
result_dict = p.create_results_dict(matchDate)

play_today_list = p.create_team_list(fixture_dict, result_dict)
#print(play_today_list)
#print(len(play_today_list))

if len(play_today_list) == 0:
    print("There are no matches today.")
else:
    tr.tweet_reader(play_today_list)
