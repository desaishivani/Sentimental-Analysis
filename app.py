from flask import Flask, render_template
from text import *


app = Flask(__name__,template_folder='template')

@app.route('/') 	
def home():
	return render_template('home.html')

@app.route('/about')
def about():
		return render_template('about.html')
		
@app.route('/contact')
def contact():
		return render_template('contact.html')
		
@app.route('/twitter')
def twitter():
		return render_template('twitter.html')
		
@app.route('/graph')
def graph():
		return render_template('graph.html')		

@app.route('/sentiment_analysis')
def sentiment_analysis():
		return render_template('sentiment_analysis.html')

@app.route('/text')
def text():
		return render_template('text.html')
		
@app.route('/t_c')
def t_c():
		return render_template('t_c.html')

#@app.route('/t_result', method=['POST'])
#def t_result():
#	if request.method == 'POST':
#		return = request.form['t_r']
#		return render_template("t_result.html",t_r=t_r)
	
if __name__ == '__main__':
	app.run(debug=True)