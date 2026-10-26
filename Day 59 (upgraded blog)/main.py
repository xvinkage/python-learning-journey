from flask import Flask, render_template
import requests

app = Flask(__name__)

URL = "https://api.npoint.io/e855b2715cf80a25a9d4"
response = requests.get(URL)
all_blogs = response.json()

@app.route("/")
def home():
    return render_template("index.html", blogs=all_blogs)
    

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post/<int:blog_id>")
def post(blog_id):
    requested_post = None
    for blog_post in all_blogs:
        if blog_post["id"] == blog_id:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == ("__main__"):
    app.run(debug=True)
