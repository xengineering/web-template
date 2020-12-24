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


import waitress
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/', methods=['POST'])
def api():
    data = request.get_json(force=True)
    print(data)
    return jsonify({"result":"ok"})


if __name__ == '__main__':
    waitress.serve(app, listen='*:8080')  # production server / bind to port
    #serve(app, unix_socket='/run/web-template/unix.sock')  # production server / unix domain socket
    #app.run()  # debug server - NOT FOR PRODUCTION!

