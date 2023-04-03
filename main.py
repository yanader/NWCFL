import date_formatting as df
import parser as p
import score_compiler
import twitter_reader as tr
import score_compiler as sc
from flask import Flask
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")

matchDate = df.custom_date()

gameday_dict = p.create_dictionary(matchDate, "fixtures")
gameday_dict.update(p.create_dictionary(matchDate, "results"))

today_team_list = p.playing_today(gameday_dict)

formatted_list = score_compiler.formatted_list(gameday_dict)

fixture_list = sc.dictionary_processor(gameday_dict)

if len(today_team_list) == 0:
    print("There are no matches today.")
else:
    tr.tweet_reader(today_team_list)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
