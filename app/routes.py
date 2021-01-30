from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Dylan'}
    posts = [
        {
            'author': {'username': 'Dylan'},
            'body': 'Beautiful day in Maine!'
        },
        {
            'author': {'username': 'Jack'},
            'body': 'I love watching Tenent!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
