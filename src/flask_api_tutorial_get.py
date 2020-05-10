from flask import Flask
from flask import jsonify
from flask import request
from src.json_load import load_json

app = Flask(__name__)
quarks = load_json("quarks.json")


# print(quarks)

@app.route('/quarks/<string:name>', methods=['GET'])
def get_one(name):
    # new_quark: object = request.get_json()
    the_one = quarks[0]
    print(the_one)
    for i, q in enumerate(quarks):
        if q['name'] == name:
            the_one = quarks[i]
    qs = request.get_json()
    return jsonify({'quarks': the_one})


if __name__ == '__main__':
    app.run(debug=True)
