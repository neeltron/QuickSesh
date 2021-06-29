from flask import Flask, render_template, request, redirect
from replit import db
import random



app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

# Index page and Rendering Basic Templates
@app.route('/', methods = ['GET', 'POST'])
def index():
  if request.method == "POST":
    id = random.randint(0, 1000)
    title = request.form.get('title')
    db[str(id)] = 'https://meet.jit.si/' + title
    print(db[str(id)])
    return redirect(db[str(id)])
  return render_template('index.html')



if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )
