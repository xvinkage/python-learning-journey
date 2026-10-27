from flask import Flask, render_template, request
import requests
import smtplib
import os
from dotenv import load_dotenv

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)





@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone_number = request.form['phone']
        message = request.form['message']
        print(f"{name}\n{email}\n{phone_number},\n{message}")
        send_email(name, email, phone_number, message)
        return render_template("contact.html", is_post="True")
    else:
        return render_template("contact.html")


def send_email(name, email, phone, message):        
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    load_dotenv()

    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(EMAIL, EMAIL, email_message)

    
if __name__ == "__main__":
    app.run(debug=True, port=5001)
