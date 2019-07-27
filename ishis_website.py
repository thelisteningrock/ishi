from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
        return render_template('main.html')

@app.route('/ishi')
def anish_related_things():
	return "This program made in GitHub is related to Ishi, obviously"

@app.route('/about')
def about_website():
	return "None available as of now."

@app.route('/contact')
def contact_thing():
	return "I am impossible to contact"

if __name__ == '__main__':
 	app.debug = True
 	port = int(os.environ.get("PORT", 5000))
 	app.run(host='0.0.0.0', port=port)

