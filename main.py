from flask import Flask, render_template, request
from replit import db
import random

def createLink(title):
  if title == "index" or title == "":
    print("you can't hack us, ha!")
  else:
    f = open("templates/" + title + ".html", "w")
    code = """
    <html>
    <head>
    <title>{}</title>
    <link href="../static/styles.css" rel="stylesheet" type="text/css" />
    <script src='https://meet.jit.si/external_api.js'></script>
    </head>
    <body>
    <iframe allow="camera; microphone; display-capture" src = "https://meet.jit.si/{}" width = "1520" height = "680">
    </iframe>
    <a href = "https://quicksesh.co/"><button id = "submit3">Leave</button></a>
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
    flag = 0
    for i in db:
      if db[i] == title:
        flag = 1
    if flag == 0:
      db[str(id)] = title
      print(db[str(id)])
      createLink(title)
      return render_template(db[str(id)] + '.html')
    else:
      createLink(title)
      return render_template(title + '.html')
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
