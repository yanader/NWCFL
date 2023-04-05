import date_formatting as df
import parser as p
import twitter_reader as tr
from flask import Flask
from views import views
import threading

def run_flask():
    app = Flask(__name__)

    app.register_blueprint(views, url_prefix="/")
    app.run(debug=True, port=8000, use_reloader=False)


def scrape_and_update():
    matchDate = df.custom_date()

    gameday_dict = p.create_dictionary(matchDate, "fixtures")
    gameday_dict.update(p.create_dictionary(matchDate, "results"))

    today_team_name_list = p.playing_today(gameday_dict)
    daily_twitter_dictionary = p.daily_twitter_dictionary(today_team_name_list)

    output_format = p.formatted_list(gameday_dict)
    fixture_list_for_processing = p.dictionary_processor(gameday_dict)

    reported_scores = []

    tr.tweet_reader(daily_twitter_dictionary, reported_scores)

##i am receiving an error message where the table-view can not access output_format.
# i think output format is what I am going to have to save to a file and then read in and process inside the view file.
# i think that will fully uncouple the processes. (i might even be able to get rid of multithreading at that point
    #if so, get rid of it and move app.run() back down beloe the 'if main' line

#before i can do that, i need to build the logic that will select the correct score.

if __name__ == "__main__":
    thread1 = threading.Thread(target=run_flask)
    thread2 = threading.Thread(target=scrape_and_update)
    thread1.start()
    thread2.start()
