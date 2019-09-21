import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    user_id = db.Column('user_id', db.Integer,
                        primary_key=True, autoincrement=True)
    username = db.Column('username', db.String(255))
    email = db.Column('email', db.String(255))
    mobile = db.Column('mobile', db.String(15))
    password_hash = db.Column('password_hash', db.String(255))

    def password(self, string):
        '''
            Generate a hashed password
        '''
        self.password_hash = generate_password_hash(
            string, method='pbkdf2:sha256')

    def verify_password(self, string):
        '''
            Check a user's password
        '''
        return check_password_hash(self.password_hash, string)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Team(db.Model):
    team_id = db.Column('team_id', db.Integer,
                        primary_key=True, autoincrement=True)
    team_name = db.Column('team_name', db.String(255))


class Worker(db.Model):
    worker_id = db.Column('worker_id', db.Integer,
                          primary_key=True, autoincrement=True)
    worker_name = db.Column('worker_name', db.String(255))
    team_id = db.Column('team_id', db.ForeignKey('team.team_id'))


class Job(db.Model):
    job_id = db.Column('job_id', db.Integer,
                       primary_key=True, autoincrement=True)
    job_title = db.Column('job_title', db.String(255))
    job_desc = db.Column('job_desc', db.Text)
    team_id = db.Column('team_id', db.ForeignKey('team.team_id'))
    worker_id = db.Column('worker_id', db.ForeignKey('worker.worker_id'))
    created_at = db.Column(
        'created_at', db.DateTime, default=datetime.datetime.utcnow)
