from flask import Flask
from flask import jsonify
from flask import request
from src.json_load import load_json

app = Flask(__name__)
quarks = load_json("quarks.json")


# print(quarks)

@app.route('/quarks', methods=['GET'])
def get_all():
    return jsonify({'quarks': quarks})


if __name__ == '__main__':
    app.run(debug=True)
