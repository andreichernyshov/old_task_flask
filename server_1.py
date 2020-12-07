from flask import Flask, url_for, render_template
import os, glob, csv, requests, sqlite3
from markupsafe import escape
from pathlib import Path
from faker import Faker
from database import exec_query


fake = Faker(['en-US'])


server_1=Flask(__name__)

DATABASE = os.path.join(os.path.dirname(__file__), 'db.sqlite3')


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
    names = [fake.unique.first_name() for i in range(100)]
    emails = list()
    for x in names:
        if len(emails) < 100:
            e_mail = f"{x} {x.lower()}@gmail.com\n"
            emails.append(e_mail)
    return render_template('generate_users.html', title=generate_users, emails=emails)


"""
p = Path("/home/zimacl/Python_")
f = p.joinpath("Python_/hw.csv")
"""


@server_1.route('/mean/')
def mean():
    ls_d = list()
    with open('hw.csv', encoding='utf-8') as data_file:
        for line in data_file:
            if len(line) <= 2:
                continue
            else:
                line = list(line.strip().split(','))
                ls_d.append(line)
        height, weight = 0, 0
        for row in range(1, len(ls_d)):
            for col in range(1, len(ls_d[0])):
                if col == 1:
                    height += float(ls_d[row][col])
                if col == 2:
                    weight += float(ls_d[row][col])
    santim_avarg = round(((height/(len(ls_d)-1)) * 2.54), 0)
    kg_avarg = round(((weight/(len(ls_d)-1))*0.45), 0)
    conten = f'Рост в см. средний = {santim_avarg}.  Вес в кг. средний = {kg_avarg}'
    return render_template('mean.html', title=mean, conten=conten)


@server_1.route('/space/')
def astro():
    r = requests.get(url='http://api.open-notify.org/astros.json')
    space = r.json()["number"]
    r_space = f'На данный момент, на МКС, находится команда из: <strong>{space}-ми человек</strong>'
    return r_space


@server_1.route('/names/')
def cus_names():
    first_names = []
    with sqlite3.connect(DATABASE) as conn:
        with conn as cursor:
            for cs_nms in cursor.execute("SELECT DISTINCT first_name FROM customers ORDER BY first_name ASC"):
                first_names.append(cs_nms)
    return render_template("names.html", first_names=first_names)


"""
@server_1.route('/users/<int:age>')
def users(age):
    users_qs = exec_query("SELECT id,username,email,age FROM users WHERE age=?", age)
    return render_template("users.html", users=users_qs)
"""

if __name__ == '__main__':
    server_1.run(debug=True)