from Flask import Flask, render_template

app = Flask(__name__)

@app.route ("/")
def index():
  headline = "Tracker"
  return render_template("index.html", headline = headline)



@app.route ("/resources")
def resources():
  headline = "COVID-19 Resources"
  return render_template("index.html", headline = headline)

app.run(host='0.0.0.0', port=8080)