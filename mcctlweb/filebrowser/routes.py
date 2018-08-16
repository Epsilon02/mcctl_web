# routes.py

from flask import render_template, Blueprint, jsonify

file_browser = Blueprint('file_browser', __name__)


@file_browser.route('/file-browser')
def get_file_browser():
    return render_template('filebrowser.jinja2')


@file_browser.route('/file-browser/id', methods=['GET', 'POST'])
def get_id():
    data = {'current': 1,
            'rowCount': 10,
            'rows': [
                {'name': 'spam',
                 "sender": "123@test.de",
                 "received": "2014-05-30T22:15:00"
                 },
                {
                    "name": 'ham',
                    "sender": "123@test.de",
                    "received": "2014-05-30T20:15:00"
                }
            ],
            'total': 2
            }
    return jsonify(data)
