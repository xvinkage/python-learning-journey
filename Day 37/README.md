# Day 37 – Intermediate – Advanced Authentication and POST/PUT/DELETE Requests

## 📚 Today's Concepts

- HTTP request methods: GET, POST, PUT, and DELETE
- API authentication using headers
- Sending data to an API using JSON
- Working with environment variables using `.env`
- Building API endpoints dynamically with Python

---

## 🛠️ What I Built

- Habit Tracker using the Pixela API
- Created a coding habit graph
- Added today's coding activity to the graph
- Used user input to determine how much I coded
- Used Python's `datetime` to generate today's date automatically
- Used `.env` to keep my Pixela token and username outside of my Python code

---

## 💡 What I Learned

- GET, POST, PUT, and DELETE are different HTTP request methods used to interact with APIs.
- POST is commonly used to create new data.
- PUT is used to update existing data.
- Authentication information can be provided through request headers.
- JSON can be used to send data in the body of a request.
- `params` sends information through the URL, while `json` sends information in the request body.
- API documentation is important because different endpoints expect data in different places.
- A common mistake is using the correct information in the wrong part of the request, such as using `params` when the API expects JSON.
- `response.text` is useful when debugging because it shows the actual response returned by the API.

---

## ⚠️ Things to Remember

- `params=` → query parameters added to the URL
- `json=` → JSON data sent in the request body
- `headers=` → metadata/authentication sent with the request
- `response` shows the HTTP response object; `response.text` shows the response content.
- Pay close attention to the exact endpoint URL required by an API.
- Date formatting matters when an API expects a specific format such as `YYYYMMDD`.
- Keep API tokens and other credentials out of source code when possible.

---

## 🚀 Key Takeaways

- APIs aren't just about sending a request — I need to understand **what the API expects and where it expects it**.
- The difference between `params`, `json`, and `headers` finally became clearer.
- PUT makes more sense as an operation for changing existing data rather than creating something completely new.
- I learned that debugging an API isn't just looking at the status code. Reading the actual response from the server can explain what went wrong.
- This knowledge will help me build automation tools that communicate with other applications and services instead of operating entirely within Python.