from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

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
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Đăng nhập', form=form)
