from flask import Flask, render_template
from yr import naa
from yr import langtidsvarsel

app = Flask(__name__)

@app.route("/")
def index():
    vær = naa(59.89, 10.52)
    return render_template("index.html", vær = vær)



