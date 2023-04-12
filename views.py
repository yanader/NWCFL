from flask import Blueprint, render_template

views = Blueprint(__name__, "views")


@views.route("/table")
def results():
    from Archive.main import output_format
    headings = ('Home', 'Score', 'Away')
    return render_template("table.html", headings=headings, data=output_format)
