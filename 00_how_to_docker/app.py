from flask import Flask, render_template
from flask import Markup

app = Flask(__name__)

@app.route("/")
def index():
    markup = Markup("<html><body><h1>Hello World</h1></body></html>")
    return markup


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
