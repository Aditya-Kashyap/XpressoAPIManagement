from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

quarks = [{'name': 'up', 'charge': '+2/3'},
          {'name': 'down', 'charge': '-1/3'},
          {'name': 'charm', 'charge': '+2/3'},
          {'name': 'strange', 'charge': '-1/3'}]


@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Hello, World!'})


@app.route('/quarks', methods=['GET'])
def return_all():
    return jsonify({'quarks': quarks})


@app.route('/quarks/<string:name>', methods=['GET'])
def return_one(name):
    the_one = quarks[0]
    for i, q in enumerate(quarks):
        if q['name'] == name:
            the_one = quarks[i]
    return jsonify({'quarks': the_one})


@app.route('/quarks', methods=['POST'])
def add_one():
    new_quark = request.get_json()
    quarks.append(new_quark)
    return jsonify({'quarks': quarks})


@app.route('/quarks/<string:name>', methods=['PUT'])
def edit_one(name):
    print(name)
    new_quark = request.get_json()
    print(f'New Entry:{new_quark}')
    for i, q in enumerate(quarks):
        if q['name'] == name:
            quarks[i] = new_quark
    qs = request.get_json()
    print(f'Request:{qs}')
    print(quarks)
    json_new = jsonify({'quarks': quarks})
    print(json_new)
    return json_new


@app.route('/quarks/<string:name>', methods=['DELETE'])
def delete_one(name):
    for i, q in enumerate(quarks):
        if q['name'] == name:
            del quarks[i]
    return jsonify({'quarks': quarks})


if __name__ == "__main__":
    app.run(debug=True)
