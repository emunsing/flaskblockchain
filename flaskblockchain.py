from flask import Flask, request, redirect, session, url_for, g, abort, render_template, flash
from flask.json import jsonify
import datetime, os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)

    return jsonify(result=range(a+b),message={'a':'apple','b':'baby','c':3})

@app.route('/')
def index():
	return render_template('ajaxTest.html')

# @app.route('/', methods=['GET'])
# def home():
# 	return render_template('home.html')


### STANDARD STUFF
@app.route('/takeaction', methods=['GET'])
def takeaction():
	return ('', 204)

@app.route('/about', methods=['GET'])
def about():
	return render_template('about.html')



@app.route('/ourtech', methods=['GET'])
def abouttech():
	return render_template('abouttech.html')

@app.route('/faqs', methods=['GET'])
def faqs():
	return render_template('FAQs.html')

@app.route('/blog1.html', methods=['GET'])
def blog1():
	return render_template('blog1.html')

@app.route('/blog2.html', methods=['GET'])
def blog2():
	return render_template('blog2.html')


if __name__ == '__main__':
	app.run(debug=True)
