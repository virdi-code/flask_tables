from flask import Flask, render_template
import csv
app = Flask(__name__)


headings = ("Symbol","Name","Price","Change")


with open('data.csv') as dataFile:
    reader = csv.reader(dataFile,delimiter=',')
    data = list(reader)

with open('datal.csv') as dataFile:
    reader = csv.reader(dataFile,delimiter=',')
    datal = list(reader)


@app.route("/")
def table():
    return render_template("table.html",headings=headings,data=data,datal=datal)


if __name__=='__main__':
    app.run(debug=True)