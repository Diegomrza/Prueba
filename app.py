from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/login', methods=['GET'])
def login():

    if request.method == "GET":

        return "Hola amigos de youtube"

@app.route('/')
def index():    
	return "Texas"

if __name__ == "__main__":
	app.run(threaded = True,port = 8000, debug = True)