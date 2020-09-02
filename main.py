#!/usr/bin/python3


"""
    web-template - A Template Project for dynamic Web Applications.

    Copyright (C) 2020  xengineering

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


from waitress import serve
from flask import Flask, render_template, current_app


app = Flask(__name__)


@app.route('/')
def index():
    return current_app.send_static_file('index.html')


@app.route('/style.css')
def style():
    return current_app.send_static_file('style.css')


@app.route('/favicon.ico')
def favicon():
    return current_app.send_static_file('favicon.ico')


if __name__ == '__main__':
    serve(app, listen='*:8080')  # production server
    #app.run()  # test server
