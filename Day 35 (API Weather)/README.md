# Day 35 – Intermediate – API Keys, Authentication, Environment Variables and Sending SMS

## 📚 Today's Concepts

- API Authentication
- API Keys
- Environment Variables
- Sending SMS with Twilio
- Using `.env` to protect credentials

---

## 🛠️ What I Built

- Built a weather notification program using the OpenWeatherMap API.
- Used an API key stored in an environment variable instead of putting it directly in the Python code.
- Retrieved weather forecast data and checked the weather condition IDs to determine if rain was expected.
- Sent a notification when rain was detected.
- Learned how Twilio can be used to send SMS messages.

---

## 💡 What I Learned

- API authentication is a way for an API to identify and authorize the application making a request.
- An API key is commonly passed as a parameter or header when making an API request.
- API keys should not be hard-coded into programs that may be shared publicly.
- Environment variables can store sensitive information such as API keys, passwords, and account credentials.
- `python-dotenv` can load values from a `.env` file into the program.
- The `.env` value returned by `os.getenv()` is a string, so it may need to be converted into the appropriate Python data type.
- Twilio provides an API for sending SMS messages.
- Reading the API documentation is important because every API has its own endpoints, parameters, authentication requirements, and response format.
- I practiced using JSON data returned from an API and extracting the information I needed.

---

## ⚠️ Things to Remember

- APIs can provide access to data or services that require authentication.
- API keys identify/authenticate an application and can also be associated with usage limits or billing, depending on the API.
- Never expose API keys, passwords, or other credentials in public code.
- Keep sensitive credentials in environment variables or another secure configuration system.
- Always read the API documentation before trying to use an unfamiliar API.
- Authentication is not always done the same way; some APIs use API keys, while others use tokens, OAuth, or other methods.
- API responses are often JSON, but the structure depends on the API.
- `os.getenv()` retrieves environment-variable values as strings.
- A Python list cannot simply be stored in a `.env` file and expected to come back as a Python list.

---

## 🚀 Key Takeaways

- **Biggest lesson:** APIs are not just about requesting data. I also need to understand how the API authenticates my program and what credentials it requires.
- **Concept that clicked:** An API key is essentially a credential that my program sends to the API so the API knows which application is making the request.
- **How this will help in future projects:** I can now start building programs that use external APIs while keeping credentials out of my source code. This will be important for the automation and business applications I want to build with Python.