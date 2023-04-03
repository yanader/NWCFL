from flask import Blueprint, render_template

import twitter_reader

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("index.html", name="Ste", age=42)


@views.route("/table")
def results():
    from main import formatted_list, today_team_list
    import twitter_reader as tr
    score = tr.tweet_reader(today_team_list)
    headings = ('Home', 'Score', 'Away')
    return render_template("table.html", headings=headings, data=formatted_list, score=score)
