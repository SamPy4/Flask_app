from flask import Flask, session, render_template, request
import jinja2
import datetime

app = Flask(__name__)

all_userids = open("users.txt", "r").read().split("\n")

def create_timestamp():
    dt = datetime.datetime(1,1,1)
    stamp = str(dt.now()).split(".")[0]
    return stamp

def test_login_inputs(usrid):
    if usrid in all_userids:
        return True
    return False

@app.route("/")
def index():
    return render_template("index.html", yee="YaaYeet")

@app.route("/login", methods=['POST'])
def login():
    log_access = 0
    if request.form['user_id']:
        login_attempts = open("login_attempts.txt", "a")
        if test_login_inputs(request.form['user_id']):
            log_access = 1
            login_attempts.write("{} ; {} ; {}\n".format(create_timestamp(), request.form['user_id'], "[OK]"))
        else:
            login_attempts.write("{} ; {} ; {}\n".format(create_timestamp(), request.form['user_id'], "[Failed]"))
    return render_template("login.html", login_access=log_access, name="null")

app.run(host="0.0.0.0", port=81, debug=True)
