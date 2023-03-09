from flask import Flask, render_template, request
from yr import naa

app = Flask(__name__)

mine_steder = []

@app.route("/", methods = ['GET', 'POST'])
def index():
    mine_steder.clear()
    if request.method == "POST":
        værdata = request.form["værdata"]
        mine_steder.append(naa(værdata))
    return render_template("index.html", mine_steder = mine_steder)


@app.route("/kommendeUke", methods = ['GET', 'POST'])
def kommendeUke():
    mine_steder.clear()
    if request.method == 'POST':
        værdata = request.form['værdata']
        mine_steder.append(kommendeUke(værdata))
    return render_template('kommendeUke.html', mine_steder = mine_steder)


@app.route("/nesteTolv", methods = ['GET', 'POST'])
def nesteTolv():
    mine_steder.clear()
    if request.method == 'POST':
        værdata = request.form['værdata']
        mine_steder.append(nesteTolv(værdata))
    return render_template('nesteTolv.html', mine_steder = mine_steder)








