from flask import Flask
from flask import jsonify
from flask import request
from src.json_load import load_json

app = Flask(__name__)

# quarks = load_json("quarks.json")
# print(quarks)

# quarks = {}
quarks = []


@app.route('/quarks', methods=['POST'])
def add_one():
    new_quark = request.get_json()
    print(type(new_quark))
    if new_quark is not None:
        x: list = {"success": True}

    quarks.append(new_quark)
    return jsonify({'quarks': x})


if __name__ == "__main__":
    app.run(debug=True)
