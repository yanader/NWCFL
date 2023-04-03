from flask import Blueprint, render_template



views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("index.html", name="Ste", age=42)




#data = main.formatted_list


@views.route("/table")
def results():
    from main import formatted_list
    headings = ('Home', 'Score', 'Away')
    return render_template("table.html", headings=headings, data=formatted_list)
