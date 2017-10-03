from flask import Flask, request, jsonify, abort
from db import db_session
from api import load_data, get_data

from functools import wraps

app = Flask(__name__)


def json_view(func):
    """Decorator that load response data to json.

    Usage:
    @app.route("/")
    @json_view
    def index(userid=None):
        pass
    """
    @wraps(func)
    def _wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        return jsonify(result)
    return _wrap


def auth_required(func):
    """Decorator that checks that requests
    contain an id-token in the request queery params.
    authentication failed, and have an id otherwise.

    Usage:
    @app.route("/")
    @authorized
    def secured_root():
        pass
    """
    @wraps(func)
    def _wrap(*args, **kwargs):
        token = request.args.get('token')
        if not token or token != '123qwe':
            # Unauthorized
            abort(401)
            return None
        return func(*args, **kwargs)
    return _wrap


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/api/incoming', methods=['POST'])
@json_view
@auth_required
def load():
    """Load bulk json data to database.
    """
    bulk = request.get_json()
    if not bulk:
        abort(400)
        result = []
    try:
        load_data(bulk)
        result = []
    except Exception as e:
        return e

    return result


@app.route('/api/datapoints', methods=['GET'])
@json_view
@auth_required
def get():
    """
    Get json data from database

    * query name: name of datapoint, String

    """
    name = request.args.get('name')
    freq = request.args.get('freq')

    if not name or not freq:
        abort(400)
        return []

    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    try:
        result = get_data(name=name, freq=freq, start_date=start_date, end_date=end_date)
    except Exception as e:
        result = e

    return result


if __name__ == '__main__':
    app.run(debug=True)