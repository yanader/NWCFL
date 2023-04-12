import date_formatting as df
import parser as p
import twitter_reader as tr
from flask import Flask
from views import views
import threading



app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")




matchDate = df.custom_date()

gameday_dict = p.create_dictionary(matchDate, "fixtures")
gameday_dict.update(p.create_dictionary(matchDate, "results"))

today_team_name_list = p.playing_today(gameday_dict)
daily_twitter_dictionary = p.daily_twitter_dictionary(today_team_name_list)

output_format = p.formatted_list(gameday_dict)
fixture_list_for_processing = p.dictionary_processor(gameday_dict)

reported_scores = []

tr.tweet_reader(daily_twitter_dictionary, reported_scores)

#### this is where i'm leaving a note. it's possible that "top=1" is a named argument we can send to
### enumerate(sntwitter.TwitterSearchScraper('from:'+twitter_handle).get_items()):
###to only get the first tweet. it may speed this up. will test.


if __name__ == "__main__":
    app.run(debug=True, port=8000, use_reloader=False)
