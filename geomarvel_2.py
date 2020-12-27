import flask
from flask import request, jsonify
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True


with open('liquidambarTrees_DC.geojson', encoding="utf8") as f:
    trees = json.load(f)
data = trees['features']


@app.route('/', methods=['GET'])
def home():
    return"<h1>The Trees of Washington DC</h1>" \
          "<p>This is a simple API that will return information" \
          "about trees in Washington DC.</p>"


@app.route('/api/v1/trees/getAll', methods=['GET'])
def getAll():
    return jsonify(data)


@app.route('/api/v1/trees/getByParam', methods=['GET'])
def getByParam():
    ward = request.args.get('ward', type=int)
    condition = request.args.get('condition', type=str)

    # WARD and CONDITION
    if 'ward' and 'condition' in request.args:
        ward = int(request.args['ward'])
        condition = str(request.args['condition'])

        results = []

        for i in data:
            if i['properties']['WARD'] == ward and i['properties']['CONDITION'] == condition:
                results.append(i)

        return jsonify(results)

    # WARD only
    elif 'ward' in request.args:
        ward = int(request.args['ward'])

        results = []

        for i in data:
            if i['properties']['WARD'] == ward:
                results.append(i)

        return jsonify(results)

    # CONDITION only
    elif 'condition' in request.args:
        condition = str(request.args['condition'])

        results = []

        for i in data:
            if i['properties']['CONDITION'] == condition:
                results.append(i)

        return jsonify(results)

    # No parameters passed
    else:
        return"<h1>No parameters passed</h1>" \
              "<p>Please specify a Ward ID or Condition...</p>"


app.run()
