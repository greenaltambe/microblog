from app import app # importing from app package the app variable

@app.route('/') # decorators : modify the function
@app.route('/index')
def index():
  return "Hello, World!"