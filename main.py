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
@app.route('/meet')
def second():
  return render_template("meet.html")



if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )
