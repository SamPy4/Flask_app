from flask import Flask, session, render_template, request
import jinja2

app = Flask(__name__)

all_users = open("users.txt", "r").read().split("\n")

def test_login_inputs(usr, pwd):
    if usr in all_users:
        if pwd == all_users[usr]:
            return True
    return False

@app.route("/")
def index():
    return render_template("index.html", yee="YaaYeet")

@app.route("/login", methods=['POST'])
def login():
    log_access = 0
    if request.form['username'] and request.form['password']:
        if test_login_inputs(request.form['username'], request.form['password']):
            log_access = 1

    return render_template("login.html", login_access=log_access, name=request.form['username'])

app.run(host="0.0.0.0", port=80, debug=True)
