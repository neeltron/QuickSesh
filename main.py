from flask import Flask, render_template, request, make_response, redirect, url_for



app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

# Index page and Rendering Basic Templates
@app.route('/')
def index():
  return render_template('index.html')



# Creating different routes
@app.route('/second')
def second():
  return "I'm on a separate route"



# HTTP Methods
@app.route('/requesthttp', methods=['GET', 'POST'])
def requesthttp():
  if request.method == 'POST':
    return "Auth here"
  else:
    return "Ask for creds here"



# File Uploads (needs an HTML Form)
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
  if request.method == 'GET':
    file = request.files['filename']
    file.save('uploads/upload.txt')



# Reading Cookies 🍪
@app.route('/readcookie')
def readcookie():
  cookie = request.cookies.get('cookie')
  return cookie



# Storing Cookies
@app.route('/storecookie')
def storecookie():
  response = make_response(render_template(index.html))
  response.set_cookie('cookie', 'whatever')
  return response
  


# Redirects
@app.route('/redirect')
def redirec():
  return redirect(url_for('index'))



if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )
