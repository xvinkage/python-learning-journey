# Day 33 – Intermediate – API Endpoints & API Parameters – ISS Overhead Notifier

## 📚 Today's Concepts

- API = Application Programming Interface
- API endpoints
- API parameters
- JSON responses
- HTTP response/status codes
- Working with data returned from an API

---

## 🛠️ What I Built

- Built an **ISS Overhead Notifier** that checks the International Space Station's current position.
- Used the ISS API to get the ISS's current latitude and longitude.
- Used the Sunrise-Sunset API to determine sunrise and sunset times.
- Added logic to determine whether the ISS is within 5 degrees of my location.
- Added logic to determine whether it is currently dark.
- Used SMTP to send an email notification telling me to look up when the conditions are met.
- Used API parameters to provide my latitude and longitude to the Sunrise-Sunset API.

---

## 💡 What I Learned

- An API is a set of rules, functions, protocols, and endpoints that programmers can use to interact with an external system or service.
- An API allows my program to send a request to an external system and receive data back.
- If my request is structured correctly, the external system can respond with the requested data.
- An **API endpoint** is the URL where my program sends its request.
- **API parameters** allow me to provide additional information or input with my request. For example, I can provide latitude and longitude to get sunrise and sunset information for a specific location.
- APIs commonly return data in **JSON**, which can be converted into Python dictionaries and other Python data types.
- `response.json()` allows me to work with JSON data in Python.
- `response.raise_for_status()` allows me to detect HTTP errors instead of continuing as if the request succeeded.
- I learned that APIs can have different requirements and parameters, so I need to read the API documentation to understand how to structure my request.
- I learned that some APIs can return information such as dates and times that need to be converted into Python data types before I can work with them.

---

## ⚠️ Things to Remember

- **API endpoint** = the URL my program sends a request to.
- **API data** is commonly returned as JSON.
- **Response/status codes** are important because they tell me whether the request succeeded or failed.
- **API parameters** allow me to provide input when making a request so the API can return different or more specific information.
- Not every API uses parameters.
- Parameters can be sent separately from the URL using the `params` argument in `requests`.
- JSON data can contain nested dictionaries and lists, so I need to understand the structure before accessing the information I need.
- I should check the API documentation instead of guessing how an endpoint or parameter works.

---

## 🚀 Key Takeaways

- **Biggest lesson:** APIs allow my Python programs to communicate with external systems and use data that I didn't have to create myself.
- **Concept that finally clicked:** An API request is basically my program asking another system for information, and the API determines how I need to ask for it.
- **How this knowledge will help in future projects:** I can use APIs to connect my Python programs to real-world services and build useful applications around external data instead of keeping everything inside my own program.