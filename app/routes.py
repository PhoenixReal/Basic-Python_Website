from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
@app.route('/login')
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
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Đăng nhập', form=form)
