from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def hello():
    user = "John"
    year = datetime.datetime.now().year
    return render_template("index.html", user=user, year=year)

@app.route("/guess/<name>")
def agify(name):
    AGE_URL = "https://api.agify.io"
    GENDER_URL = "https://api.genderize.io"

    params = {
        "name": name,
    }
    
    age_response = requests.get(AGE_URL, params=params)
    print(age_response)
    print(age_response.json())
    age = age_response.json()["age"]

    gender_response = requests.get(GENDER_URL, params=params)
    gender = gender_response.json()["gender"]
    return render_template("agify.html", name_input=name, gender=gender, age=age)

@app.route("/blog")
def blog():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
   
    return render_template("blog.html", posts=all_posts)




if __name__ == "__main__":
    app.run(debug=True)