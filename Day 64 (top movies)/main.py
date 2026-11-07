from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, URLField, DateField, FloatField, IntegerField
from wtforms.validators import DataRequired, URL, NumberRange
import requests
from dotenv import load_dotenv
import os
# from datetime import datetime

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
URL="https://api.themoviedb.org/3/search/movie"
URL_DETAIL="https://api.themoviedb.org/3/movie"
IMAGE_URL = "https://image.tmdb.org/t/p/w500"
headers = {
            "Authorization": API_TOKEN
            }

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)



# CREATE DB


# CREATE TABLE
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top-movies.db"
# initialize the app with the extension
db.init_app(app)

class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True, autoincrement=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()
#     new_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )
#     db.session.add(new_movie)
#     db.session.commit()


class MovieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    # year = IntegerField('Year', validators=[DataRequired(), NumberRange(min=1900, max=datetime.now().year)])
    # description = StringField('Description', validators=[DataRequired()])
    # rating = FloatField('Your rating Out of 10 (e.g. 7.5)', validators=[DataRequired(), NumberRange(min=1)], render_kw={"step": "0.1", "min": "1", "max": "10"})
    # ranking = IntegerField('Ranking', validators=[DataRequired(), NumberRange(min=1)])
    # review = StringField('Review', validators=[DataRequired()])
    # img_url = URLField('Image URL', validators=[DataRequired(), URL()])

    submit = SubmitField('Add Movie')

class RateMovieForm(FlaskForm):
    rating = FloatField('Your rating Out of 10 (e.g. 7.5)', validators=[DataRequired(), NumberRange(min=1)], render_kw={"step": "0.1", "min": "1"})
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Submit')



@app.route("/")
def home():
    all_movies = db.session.execute(db.select(Movie).order_by(Movie.rating.desc())).scalars().all()

    for num in range(len(all_movies)):
        all_movies[num].ranking = len(all_movies) - num
    db.session.commit()
    
    return render_template("index.html", all_movies=all_movies)

@app.route("/edit/<int:id>", methods=["POST", "GET"])
def edit(id):
    form = RateMovieForm()
    if request.method == "GET": 
       db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
    else:
        # movie_to_update = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
        movie_to_update = db.get_or_404(Movie, id)  
        movie_to_update.rating = form.rating.data
        movie_to_update.review = form.review.data

        db.session.commit()  
        return redirect(url_for('home'))        
    return render_template('edit.html', form=form, id=id)

@app.route("/delete/<int:id>", methods=["GET"])
def delete(id):
    if request.method == "GET":
        # movie_to_delete = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
        movie_to_delete = db.get_or_404(Movie, id)  
        db.session.delete(movie_to_delete)
        db.session.commit() 
    return redirect(url_for('home'))

@app.route("/add", methods=["POST", "GET"])
def add():
    form = MovieForm()
    if request.method == "POST" and form.validate_on_submit():
        title = form.title.data
        print(title)
        params = {
            "query":title
        }

        response = requests.get(URL, headers=headers, params=params)
        movies = response.json()["results"]
       
        # new_movie = Movie(title=title)
        # db.session.add(new_movie)
        # db.session.commit()
        return render_template("select.html", movies=movies)

    return render_template("add.html", form=form)

@app.route("/select/<int:id>", methods=["GET", "POST"])
def select(id):
    if request.method == "GET":
        response = requests.get(f"{URL_DETAIL}/{id}", headers=headers)
        movie_details = response.json() #["belongs_to_collection"]
        title = movie_details["title"]
        img_url = f"{IMAGE_URL}{movie_details["poster_path"]}"
        year = movie_details["release_date"]
        description = movie_details["overview"]

        new_movie = Movie(title=title, year=year, description=description, img_url=img_url)
        db.session.add(new_movie)
        db.session.commit()
    return redirect(url_for('edit', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
