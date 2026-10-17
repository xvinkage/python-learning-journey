from flask import Flask

app = Flask(__name__)

def bold(function):
    def wrapper():
        return f"<strong>{function()}</strong>"
    return wrapper

def emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper

def underline(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper

@app.route("/")
@bold
@emphasis
@underline
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)