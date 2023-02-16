from flask import Flask, render_template
from yr import naa



app = Flask(__name__)

@app.route("/")
def index():
    sted="sandvika"
    vær = naa(sted)
    return render_template("index.html", vær = vær, sted=sted)



