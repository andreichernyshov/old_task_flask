from flask import Flask, url_for, render_template
import os, glob
from markupsafe import escape

server_1=Flask(__name__)



@server_1.route('/')
def index():
    return 'Index Page'


@server_1.route('/requirements/')
def requirements():
    return render_template('requirements.html', title=requirements, req=req)


req = list()
with open('requirements.txt') as packejes:
    for i in packejes:
        i = f"{i} "
        req.append(i)


@server_1.route('/generate_users/')
def generate_users():
    return render_template('generate_users.html', title=generate_users, us_ml=us_ml)


us_ml = list()
with open('fake_list.txt') as usr_mail:
    for x in usr_mail:
        x = f"{x} "
        us_ml.append(x)


if __name__ == "__main__":
    server_1.run(debug=True)