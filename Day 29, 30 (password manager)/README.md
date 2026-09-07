# Day 30 – Intermediate – Errors, Exceptions and JSON Data

## 📚 Today's Concepts

- Handling Errors & Exceptions
- `try`, `except`, `else`, and `finally`
- Common exceptions such as `FileNotFoundError`, `KeyError`, and `JSONDecodeError`
- Raising your own exceptions with `raise`

---

## 🛠️ What I Built

- Improved my Password Manager project
- Added JSON data storage so passwords could be saved and retrieved
- Added password search functionality using dictionary lookups
- Added error handling so the program doesn't crash when a data file or website isn't found
- Added confirmation dialogs before saving passwords

---

## 💡 What I Learned

- Catch exceptions so your code doesn't just break using `try`, `except`, `else`, and `finally`
- `FileNotFoundError` happens when trying to access a file that doesn't exist
- `KeyError` happens when trying to access a dictionary key that doesn't exist
- `else` runs when the `try` block succeeds without an exception
- `finally` runs regardless of whether an exception occurs
- `raise` can be used to intentionally create an exception with my own message
- JSON can be loaded from a file into a Python object with `json.load()`
- Python data can be saved back to JSON with `json.dump()`
- A better solution isn't always about preventing every error — it's about handling expected errors appropriately

---

## ⚠️ Things to Remember

- Put the code that might cause the exception inside the `try` block
- Use the appropriate exception type in `except`
- `else` is useful for code that should only run when the `try` succeeds
- `finally` runs whether an exception happens or not
- `data[key]` can raise a `KeyError` if the key doesn't exist
- `json.load()` can raise `JSONDecodeError` if the JSON is empty or invalid
- `"a"` mode doesn't work like normal text appending when working with JSON objects
- `data.update()` changes the dictionary in memory; the changes still need to be written back to the JSON file
- When raising an exception yourself, provide a useful error message

---

## 🚀 Key Takeaways

- The biggest lesson from today was learning how to make programs handle problems instead of immediately crashing.
- `try/except` finally clicked for me as a way to anticipate problems that can realistically happen while my program is running.
- Understanding different exception types will make debugging easier because I can identify what actually went wrong.
- JSON combined with exception handling gives me a foundation for building programs that can save, retrieve, and safely manage data.
- These concepts will be useful in future automation and business applications where programs need to deal with missing files, invalid data, and unexpected user input.