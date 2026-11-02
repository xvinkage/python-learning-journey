from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from sqlalchemy import Integer, String, Float, create_engine



class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)



@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    return render_template('index.html', all_books=all_books)



@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book = request.form.get("book_name")
        author = request.form.get("book_author")
        rating = request.form.get("rating")
        

        db.create_all()

        new_book = Book(title=book, author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('add.html')

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    if request.method == "GET":
        book = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
    else:
        book_to_update = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
        # or book_to_update = db.get_or_404(Book, book_id)  
        book_to_update.rating = request.form.get("rating")
        db.session.commit()  
        return redirect(url_for('home'))

    return render_template('edit.html', id=id, book=book)

if __name__ == "__main__":
    app.run(debug=True)

