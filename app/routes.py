from flask import render_template, flash, redirect, url_for
from app import app # importing from app package the app variable
from app.forms import LoginForm

@app.route('/') # decorators : modify the function
@app.route('/index')
def index():
  user = {'username': 'Greenal'}
  posts = [
    {
      'author': {'username': 'John'},
      'body': 'Beautiful day in Portland!'
    }, 
    {
      'author': {'username': 'Susan'},
      'body': 'The Avengers movie was so cool!'
    }
  ]
  return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
    return redirect(url_for('index'))
  return render_template('login.html', title='Sign In', form=form)