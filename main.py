from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html', title='Home Page')

@app.route('/home')
def home():
    return render_template('home.html', title='Home Page')

@app.route('/about')
def about():
    return render_template('about.html', title='About Us')

@app.route('/links')
def links():
    return render_template('links.html', title='Links')

if __name__ == "__main__":
    app.run()