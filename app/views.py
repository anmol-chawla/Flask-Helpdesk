from flask import render_template, request
from app import app


@app.route('/', methods=['GET'])
def login_page():
    return render_template("login.html")


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'test' and password == '1234':
        return render_template("base.html")
    else:
        return render_template("wrong_login.html")


@app.route('/register', methods=['GET'])
def register():
    return render_template("register.html")


@app.route("/registration", methods=['POST'])
def registration():
    usernmae = request.form.get('username')
    password = request.form.get('password')
    mobile = request.form.get('mobile')
    email = request.form.get('email')
    render_template("base.html")


@app.route('/main', methods=['GET'])
def main_page():
    return render_template("main.html")


teams = [{
    'number': 1,
    'team_name': 'IT',
    'jobs_assigned': 5
},
    {
    'number': 2,
    'team_name': 'Marketing',
    'jobs_assigned': 4
}
]

workers = [{
    'number': 1,
    'worker_name': 'Alvin',
    'team_name': 'IT'
},
    {
    'number': 2,
    'worker_name': 'Kirk',
    'team_name': 'Marketing'
}
]

jobs = [{
    'number': 1,
    'job_title': 'Internet',
    'job_description': 'Internet is not working',
    'team_assigned': 'IT'
},
{
    'number': 2,
    'job_title': 'Sales',
    'job_description': 'The sales of products is going down',
    'team_assigned': 'Marketing'
}]

@app.route('/teams', methods=['GET'])
def main_team():
    return render_template('teams.html', teams=teams)


@app.route('/workers', methods=['GET'])
def main_worker():
    return render_template('workers.html', workers=workers)


@app.route('/jobs', methods=['GET'])
def main_jobs():
    return render_template('jobs.html', jobs=jobs)

@app.route('/about', methods=['GET'])
def main_about():
    return render_template('about.html')

@app.route('/credits', methods=['GET'])
def main_credits():
    return render_template('credits.html')
