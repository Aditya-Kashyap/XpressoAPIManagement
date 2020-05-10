from flask import Flask

app = Flask(__name__)


# app.route(rule, options)
# The rule parameter represents URL binding with the function.
# The options is a list of parameters to be forwarded to the underlying Rule object.
# @app.route("/api/v1/users/", methods=['GET', 'POST', 'PUT'])
# default is GET
# https://hackersandslackers.com/flask-routes/
@app.route('/')
def hello_world():
    return "A"


if __name__ == '__main__':
    app.run()
