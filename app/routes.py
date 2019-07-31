from flask import render_template, request
from app import app


@app.route('/')
def login_page():
    return render_template("login.html", show_header=False)


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'test' and password == '1234':
        return render_template("base.html")
    else:
        return render_template("wrong_login.html")


@app.route('/register')
def register():
    return render_template("register.html", show_header=False)


@app.route("/registration", methods=['POST'])
def registration():
    usernmae = request.form.get('username')
    password = request.form.get('password')
    mobile = request.form.get('mobile')
    email = request.form.get('email')
    render_template("base.html")
