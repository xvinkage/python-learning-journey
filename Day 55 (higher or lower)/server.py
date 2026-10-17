from flask import Flask
import random

app = Flask(__name__)

random_num = 0
def gen_numer():
    global random_num
    random_num = random.randint(0,9)


gen_numer()

@app.route("/")
def home():
    return "<h1> Guess a number between 0 and 9 </h1> \
    <img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route("/<int:guess>")
def guess(guess):
    if guess < random_num:
        return "<h1 style='color: red;'> Too low </h1> \
        <img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"

    elif guess > random_num:
        return "<h1 style='color: purple;'> Too High </h1> \
        <img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return "<h1 style='color: green;'> Your guess is correct </h1> \
        <img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"

if __name__ == "__main__":
    app.run(debug=True)