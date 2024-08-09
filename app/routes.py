from flask import render_template
from app import app 

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Phoenix'}
    posts = [
        {
            'author': {'username': 'Thuận'},
            'body': 'Sv aya!'
        },
        {
            'author': {'username': 'Đan'},
            'body': 'Van heo đi top!'
        }
    ]
    return render_template('index.html', title='Trang chủ', user=user, posts=posts)

