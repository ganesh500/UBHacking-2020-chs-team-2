from flask import Flask, render_template
app = Flask(__name__)

@app.route ("/")
def index():
  headline = "COVID-19 Tracker"
  return render_template("index.html", headline = headline)

@app.route ("/")
def body():
  import graph.py
  return render_template("index.html", graph = graph)



@app.route ("/")
def resources():
  headline = "COVID-19 Resources"
  return render_template("index.html", headline = headline)

app.run(host='0.0.0.0', port=8080)