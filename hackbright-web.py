from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get ("github", "jhacks")
    first, last, github = hackbright.get_student_by_github(github)
    project_info = hackbright.get_grades_by_github(github)
    html = render_template("student_info.html",
    						first=first,
    						last=last,
    						github=github,
    						project_info=project_info)

    return html

@app.route("/student_search")
def get_student_form():
	"""Show form for searching for a student."""

	return render_template("student_search.html")

@app.route("/display_form")
def display_form():

	return render_template("new_student.html")

@app.route("/student_add", methods=['POST'])
def student_add():
	firstname = request.form.get ('firstname')
	lastname = request.form.get ('lastname')
	githubname = request.form.get ('githubname')

	return render_template("added_student.html",
							firstname=firstname,
							lastname=lastname,
							githubname=githubname)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
