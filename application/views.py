from flask import request, jsonify, abort


from application import app, json_view, auth_required, api, db



@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()


@app.route('/api/incoming', methods=['POST'])
@json_view
@auth_required
def load():
    """Load bulk json data to database.
    """
    bulk = request.json
    if not bulk:
        abort(400)
        result = []
    try:
        api.load_data(bulk)
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
        result = api.get_data(name=name, freq=freq, start_date=start_date, end_date=end_date)
    except Exception as e:
        result = e

    return result


if __name__ == '__main__':
    app.run(debug=True)