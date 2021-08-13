from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    s = "<p>Hello, World! Flask is here</p>"
    s += " <p>and some more stuff</p>"

if __name__ == "__main__":
    app.run()