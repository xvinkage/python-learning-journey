# Day 54 – Intermediate – Introduction to Web Development with Flask

## 📚 Today's Concepts
- Flask and web development
- Client, server, and database architecture
- Python decorators
- First-class functions, nested functions, and returning functions

---

## 🛠️ What I Built
- **Flask application:** Created a basic web application that returns `"Hello, World!"` when visiting the homepage.
- **Execution-time decorator:** Built a decorator that measures how long a function takes to execute.
- **Function performance comparison:** Applied the decorator to `fast_function()` and `slow_function()` to compare the execution times of loops with one million and ten million iterations.
- **Fixed a timing issue:** Moved `time.time()` inside the wrapper function so each function call gets its own starting timestamp.

---

## 💡 What I Learned
- **Backend architecture:** A typical web application involves a client, a server, and often a database. The client sends requests, the server processes them, and the database stores or retrieves information when needed.
- **Frameworks:** A framework provides structure and tools for building applications. Flask and Django are Python web development frameworks.
- **Flask:** Flask lets me create web applications and define how the application responds to different URLs.
- **Routes:** `@app.route("/")` connects the homepage URL to a Python function.
- **Flask application object:** `app = Flask(__name__)` creates the application instance.
- **Running Flask:** `app.run()` starts Flask's development server.
- **The `__name__` variable:** `if __name__ == "__main__":` checks whether the Python file is being executed directly, allowing the development server to start under that condition.
- **First-class functions:** Python functions are objects. They can be assigned to variables, passed as arguments to other functions, and returned from functions.
- **Nested functions:** A function can be defined inside another function.
- **Returning functions:** A function can return another function instead of executing it immediately.
- **Decorators:** A decorator wraps a function to add functionality without changing the original function's code.
- **The `@` decorator syntax:** `@speed_calc_decorator` applies the decorator to a function, effectively replacing the function's name with the wrapper it returns.
- **Measuring execution time:** `time.time()` returns the current Unix timestamp. Subtracting a starting timestamp from an ending timestamp gives the elapsed time in seconds.
- **Scope and timing:** Placing `current_time = time.time()` inside the wrapper ensures each function call starts with a fresh timestamp.
- **F-strings:** Numeric formatting such as `:.4f` can display a floating-point value to four decimal places.

---

## ⚠️ Things to Remember
- Start the Flask development server with `flask --app name run`, replacing `name` with the Python filename without `.py`.
- On Windows, `set FLASK_APP=name.py` configures the Flask application for the current Command Prompt session when using the older `flask run` approach.
- `@app.route("/")` defines the route; the function below it provides the response.
- `return` sends a value back from a function. In a Flask route, the returned value becomes the response sent to the client.
- A decorator commonly accepts a function, defines a wrapper, and returns that wrapper.
- Calling `function()` executes the original function. Passing `function` without parentheses passes the function object itself.
- `continue` skips to the next iteration of the current loop, while `break` exits the current loop.
- For execution-time measurements, record the start time immediately before the operation and subtract it from the end time.
- Use decorators when you want to add reusable behavior, such as timing or logging, to multiple functions.

---

## 🚀 Key Takeaways
- **Biggest lesson:** I can extend the behavior of existing functions using decorators instead of rewriting their logic.
- **Concept that clicked:** Functions can be passed into other functions, defined inside them, and returned from them. This is what makes decorators possible.
- **Practical application:** I can measure how long automation scripts take to execute and later use Flask to create a web interface for Python projects.
- **Future direction:** Combining Flask with Python automation could let me build simple web applications that display results, accept user input, and trigger backend tasks.
