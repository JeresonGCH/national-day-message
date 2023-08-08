from flask import Flask, render_template, request

app = Flask(__name__)


@app.route(
  '/', methods=["GET", "POST"]
)  ##post is storing the data in python, get is trying to read data from python itself
def index():
  if request.method == "POST":  ##using post here because in html file, we are using post. Basically, python is checking if the file is post, it will store the messages. else, it will return the messages
    message = request.form['message']
    with open('messages.txt', 'a') as file:
      file.write(message + "\n")  ##storing every message on a different line
      ##file close
    return render_template("index.html", message=message)
    ##the following lines are for when the method is "get"
  with open('messages.txt', 'r') as file:
    posts = file.readlines()
  return render_template("index.html", posts=posts)


app.run(host='0.0.0.0', port=81)
