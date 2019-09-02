import datetime

from flask import render_template, request, redirect, url_for
from app import app


@app.route('/', methods=['GET'])
def login_page():
    return render_template("login.html")


@app.route('/register', methods=['GET'])
def register():
    return render_template("register.html")



@app.route('/main', methods=['GET'])
def main_page():
    return render_template("main.html")


teams = [{
    'id': 1,
    'team_name': 'IT',
    'jobs_assigned': 5
},
    {
    'id': 2,
    'team_name': 'Marketing',
    'jobs_assigned': 4
}
]

workers = [{
    'id': 1,
    'worker_name': 'Alvin',
    'team_name': 'IT'
},
    {
    'id': 2,
    'worker_name': 'Kirk',
    'team_name': 'Marketing'
}
]

jobs = [{
    'id': 1,
    'job_title': 'Internet',
    'job_description': 'Internet is not working',
    'team_assigned': 'IT',
    'created_at': datetime.datetime.now().strftime("%a, %d %b %Y")
},
    {
    'id': 2,
    'job_title': 'Sales',
    'job_description': 'The sales of products is going down',
    'team_assigned': 'Marketing',
    'created_at': datetime.datetime.now().strftime("%a, %d %b %Y")

}]


@app.route('/teams', methods=['GET'])
def main_team():
    return render_template('teams.html', teams=teams)


@app.route('/workers', methods=['GET'])
def main_worker():
    return render_template('workers.html', workers=workers, teams=teams)


@app.route('/jobs', methods=['GET'])
def main_jobs():
    teams = {
        '1': {
            'id': 1,
            'name': 'IT',
            'workers': [{'id': 1, 'name': 'Alvin'}, {'id': 2, 'name': 'Mark'}]
        },
        '2': {
            'id': 2,
            'name': 'Marketing',
            'workers': [{'id': 1, 'name': 'Kirk'}]
        }
    }
    return render_template('jobs.html', jobs=jobs, teams=teams)


@app.route('/about', methods=['GET'])
def main_about():
    return render_template('about.html')


@app.route('/credits', methods=['GET'])
def main_credits():
    return render_template('credits.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'test' and password == '1234':
        return redirect(url_for('main_page'))
    else:
        return render_template("wrong_login.html")


@app.route("/registration", methods=['POST'])
def registration():
    usernmae = request.form.get('username')
    password = request.form.get('password')
    mobile = request.form.get('mobile')
    email = request.form.get('email')
    return redirect(url_for(login_page))


@app.route('/add/team', methods=['POST'])
def add_team():
    team_name = request.form.get('teamname')
    print(team_name)
    return redirect(url_for('main_page'))


@app.route('/add/worker', methods=['POST'])
def add_worker():
    worker_name = request.form.get('workername')
    team_id = request.form.get('team')
    print(worker_name, team_id)
    return redirect(url_for('main_page'))


@app.route('/add/job', methods=['POST'])
def add_job():
    job_title = request.form.get('jobtitle')
    job_desc = request.form.get('jobdesc')
    team_id = request.form.get('team')
    worker_id = request.form.get('worker')
    print(job_title, job_desc, team_id, worker_id)
    return redirect(url_for('main_page'))
