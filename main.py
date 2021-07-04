from flask import Flask, render_template, request, redirect
from replit import db
import random

def createLink(title):
  f = open("templates/" + title + ".html", "w")
  code = """
  <html>
  <head>
  <title>{}</title>
  </head>
  <body>
  <a href = "https://letsdosome.tech">Back</a>
  <iframe src = "https://meet.jit.si/{}" width = "1520" height = "680">
  </iframe>
  </body>
  </html>
  """.format(title, title)
  f.write(code)



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
    db[str(id)] = title
    print(db[str(id)])
    createLink(title)
    return render_template(db[str(id)]+'.html')
  return render_template('index.html', obj = db)



@app.route('/join', methods = ['GET', 'POST'])
def join():
  title = request.args.get('title')
  if title != None:
    return render_template(str(title)+'.html')

if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )
