from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def page_main():
    return render_template("one.html")

app.run()
