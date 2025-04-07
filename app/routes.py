from flask import render_template
from app import app # importing from app package the app variable

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