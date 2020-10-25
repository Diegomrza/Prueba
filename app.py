from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

@app.route('/', methods=['POST'])
def login():

    if request.method == "POST":

        return '<h1>Hola amigos de youtube</h1>'

@app.route('/login', methods=['POST'])
def index():
	return "<h1>Texas</h1>"

if __name__ == "__main__":
	app.run(threaded = True,port = 8000, debug = True)