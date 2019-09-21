import datetime

from flask import render_template, request, redirect, url_for, session
from app import app, db
from .models import User, Team, Worker, Job


@app.route('/', methods=['GET'])
def login_page():
    return render_template("login.html")


@app.route('/register', methods=['GET'])
def register():
    return render_template("register.html")


@app.route('/main', methods=['GET'])
def main_page():
    page = request.args.get('page')
    if page is None:
        page = 'teams'
    return render_template("main.html", page=page)


@app.route('/teams', methods=['GET'])
def main_team():
    teams = []
    db_teams = Team.query.all()
    for team in db_teams:
        dic = {
            'id': team.team_id,
            'team_name': team.team_name,
            'jobs_assigned': Job.query.filter_by(team_id=team.team_id).count()
        }
        teams.append(dic)
    return render_template('teams.html', teams=teams)


@app.route('/workers', methods=['GET'])
def main_worker():
    teams = []
    db_teams = Team.query.all()
    for team in db_teams:
        dic = {
            'id': team.team_id,
            'team_name': team.team_name,
            'jobs_assigned': Job.query.filter_by(team_id=team.team_id).count()
        }
        teams.append(dic)
    workers = []
    db_workers = Worker.query.all()
    for worker in db_workers:
        dic = {
            'id': worker.worker_id,
            'worker_name': worker.worker_name,
            'team_name': Team.query.filter_by(team_id=worker.team_id).first().team_name
        }
        workers.append(dic)
    return render_template('workers.html', workers=workers, teams=teams)


@app.route('/jobs', methods=['GET'])
def main_jobs():
    jobs = []
    db_jobs = Job.query.all()
    for job in db_jobs:
        dic = {
            'id': job.job_id,
            'job_title': job.job_title,
            'job_description': job.job_desc,
            'team_assigned': Team.query.filter_by(team_id=job.team_id).first().team_name,
            'worker_assigned': Worker.query.filter_by(team_id=job.team_id, worker_id=job.worker_id).first().worker_name,
            'created_at': job.created_at.strftime("%a, %d %b %Y")
        }
        jobs.append(dic)
    teams = {}
    db_teams = Team.query.all()
    for team in db_teams:
        db_workers = Worker.query.filter_by(team_id=team.team_id).all()
        workers = []
        for worker in db_workers:
            dic = {}
            dic['id'] = worker.worker_id
            dic['name'] = worker.worker_name
            workers.append(dic)
        teams[team.team_id] = {
            'id': team.team_id,
            'name': team.team_name,
            'workers': workers
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
    try:
        user = User.query.filter_by(username=username).first()
        if user.verify_password(password):
            return redirect(url_for('main_page', page='teams'))
        else:
            return render_template("wrong_login.html")
    except Exception as e:
        return render_template("wrong_login.html")


@app.route("/registration", methods=['POST'])
def registration():
    username = request.form.get('username')
    password = request.form.get('password')
    mobile = request.form.get('mobile')
    email = request.form.get('email')
    new_user = User(
        username=username,
        mobile=mobile,
        email=email
    )
    new_user.password(password)
    with app.app_context():
        db.session.add(new_user)
        db.session.commit()
    return redirect(url_for('login_page'))


@app.route('/add/team', methods=['POST'])
def add_team():
    team_name = request.form.get('teamname')
    new_team = Team(team_name=team_name)
    with app.app_context():
        db.session.add(new_team)
        db.session.commit()
    return redirect(url_for('main_page', page='teams'))


@app.route('/add/worker', methods=['POST'])
def add_worker():
    worker_name = request.form.get('workername')
    team_id = request.form.get('team')
    new_worker = Worker(
        worker_name=worker_name,
        team_id=team_id
    )
    with app.app_context():
        db.session.add(new_worker)
        db.session.commit()
    return redirect(url_for('main_page', page='workers'))


@app.route('/add/job', methods=['POST'])
def add_job():
    job_title = request.form.get('jobtitle')
    job_desc = request.form.get('jobdesc')
    team_id = request.form.get('team')
    worker_id = request.form.get('worker')
    new_job = Job(
        job_title=job_title,
        job_desc=job_desc,
        team_id=team_id,
        worker_id=worker_id)
    with app.app_context():
        db.session.add(new_job)
        db.session.commit()
    return redirect(url_for('main_page', page='jobs'))
