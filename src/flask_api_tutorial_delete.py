from flask import Flask
from flask import jsonify
from flask import request
from src.json_load import load_json

app = Flask(__name__)
quarks = load_json("quarks.json")


# print(quarks)

@app.route('/quarks/<string:name>', methods=['DELETE'])
def delete_one(name):
    new_quark: object = request.get_json()
    for i, q in enumerate(quarks):
        if q['name'] == name:
            print(q['name'])
            del quarks[i]
    # qs = request.get_json()
    print(quarks)
    return jsonify({'quarks': quarks})


if __name__ == '__main__':
    app.run(debug=True)
