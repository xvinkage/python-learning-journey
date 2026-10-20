# Day 56–57 – Flask, Jinja Templates, and Dynamic Blog Pages

## 📚 Concepts Learned
- Flask web development
- Jinja templating
- Rendering HTML templates
- Passing Python variables into HTML
- Jinja expressions and statements
- Dynamic URL routing
- Building URLs with `url_for()`
- Fetching JSON data from an API

---

## 🛠️ What I Built
- **Personal blog homepage:** Created a Flask homepage that retrieves blog posts from an API and displays them as cards.
- **Dynamic blog links:** Added a “Read” link to each post that navigates to a URL containing that post's ID.
- **Individual blog pages:** Created a separate HTML template to display a selected post's title and subtitle.
- **API integration:** Used Python's `requests` library to retrieve blog post data as JSON.
- **Template rendering:** Used Flask's `render_template()` to pass data from Python into HTML.

---

## 💡 What I Learned

### Jinja Templates
- Jinja allows Python application data to be displayed dynamically inside HTML templates.
- Double curly braces `{{ }}` evaluate an expression and render its result in the HTML.
- Variables must be passed from Python using `render_template()` before they can be accessed by name in the template.

Example:
```python
return render_template("index.html", user=user, year=year)
```

In the HTML template:
```html
<p>Hello, {{ user }}!</p>
<p>{{ year }}</p>
```

### Jinja Statements
- `{% %}` is used for template statements such as loops and conditional logic.
- A `for` loop can iterate over a list passed from Python.
- Loops must be closed with `{% endfor %}`.

Example:
```html
{% for post in posts %}
    <h2>{{ post["title"] }}</h2>
{% endfor %}
```

### URL Building with Flask
- `url_for()` generates a URL for a Flask view function.
- It is useful when creating links between pages.
- Dynamic route parameters can be passed into `url_for()`.

Example:
```html
<a href="{{ url_for('blog_post', blog_id=post['id']) }}">Read</a>
```

This creates a link to the `blog_post` route using the ID of the current post.

### Dynamic Routes
- Flask can capture values from a URL using route parameters.
- Example: `/post/<blog_id>` passes the URL value into the `blog_id` function argument.
- The application can use that ID to find the correct post.

### API Requests and JSON
- `requests.get()` retrieves data from an API.
- `response.json()` converts a JSON response into Python data structures, such as lists and dictionaries.
- A list of dictionaries can be looped through to display multiple blog posts.

---

## ⚠️ Things to Remember
- `{{ }}` displays the result of an expression.
- `{% %}` executes a Jinja template statement.
- Use `{% endfor %}` to close a Jinja loop.
- Variables passed into `render_template()` must match the names used in the template.
- Use `posts` when working with a list of posts and `post` when displaying one individual post.
- A URL parameter such as `blog_id` is a string by default unless a route converter specifies another type.
- `url_for()` uses the **Python view function's name**, not the HTML filename.
- `response.json()` requires a valid JSON response.
- When accessing a post by ID, find the matching dictionary in the list before rendering the individual post page.

---

## 🚀 Key Takeaways
- **Biggest lesson:** Flask and Jinja connect Python logic and data to HTML pages.
- **Concept that clicked:** Jinja can dynamically display Python variables and loop through collections directly inside HTML.
- **Practical application:** I can retrieve data from an API and display it as a blog website with a homepage and individual post pages.
- **Future applications:** These skills can help me build dashboards and web interfaces for Python automation projects.

---

## 🧠 Skills Practiced
- Python functions and variables
- Lists and dictionaries
- Loops and conditional logic
- HTTP requests
- JSON parsing
- Flask routing
- Jinja templating
- HTML and anchor tags
- Passing data between Python and HTML

