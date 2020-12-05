from flask import Flask, url_for, render_template
import os, glob, csv
from markupsafe import escape
from pathlib import Path

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


if __name__ == "__main__":
    server_1.run(debug=True)