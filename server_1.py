from flask import Flask, url_for, render_template
import os, glob
from markupsafe import escape

server_1=Flask(__name__)

req = list()
with open('requirements.txt') as packejes:
    for line in packejes:
        line = f"{line} "
        req.append(line)


@server_1.route('/')
def index():
    return 'Index Page'


@server_1.route('/requirements/')
def requirements():
    return render_template('requirements.html', title=requirements, req=req)

     
if __name__ == "__main__":
    server_1.run(debug=True)