from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html')
	
@app.route('/blog')
def blog_thing():
	return render_template('blog.html')

@app.route('/about')
def about_thing():
	return "Everything you could possibly want to know can be found by searching."
	

@app.route('/contact')
def contact_thing():
	return "I am impossible to contact, aside from emails, social media etc."

@app.route('/play')
def fun_thing():
	return render_template('contact.html')

def test_thing():
	return "I am impossible to contact, aside from emails, forums, places I edit etc."
if __name__ == '__main__':
 	app.debug = True
 	port = int(os.environ.get("PORT", 5000))
 	app.run(host='0.0.0.0', port=port)
	

