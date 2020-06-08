from flask import render_template, url_for, flash, redirect
from my_blog import app
from my_blog.forms import LoginForm, RegistrationForm
from my_blog.models import User, Post


posts = [
    {
        'author': 'Abdulmalik Giwa',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'May 19, 2020'
    },
    {
        'author': 'Mustapha Baruwa',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'May 20, 2020'
    }
]


@app.route("/")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data} !', 'success')
        return redirect(url_for('home'))
    return render_template('registration.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('Login Successful', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Fail', 'danger')

    return render_template('login.html', title='Login', form=form)

