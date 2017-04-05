from flask import Flask, request, redirect, session, url_for, g, abort, render_template, flash
from flask.json import jsonify
import datetime, os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

@app.route('/', methods=['GET'])
def home():
	return ("Hello World! It is currently %s"%datetime.datetime.now() )

if __name__ == '__main__':
	app.run(debug=True)
