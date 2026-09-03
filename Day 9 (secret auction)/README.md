# Day 9 – Beginner – Dictionaries and Nesting

## 📚 Today's Concepts

- Dictionaries
- Loop through a dictionary gives you the key
- Nesting dictionaries and lists within dictionaries
- A dictionary value can be a list with multiple entries
- Using `max()` with `key=`
- Accessing dictionary values using keys
- Comparing values stored in a dictionary

---

## 🛠️ What I Built

- Grading program
- Blind auction program
- Feature I implemented
  - Stored bidder names and bids in a dictionary
  - Allowed multiple bidders using a while loop
  - Determined the highest bidder
  - Displayed the winner and winning bid
- Problem I solved
  - Figured out how to find the highest value in a dictionary using `max(bids, key=bids.get)`

---

## 💡 What I Learned

- Dictionaries consist of keys and values `{Key: Value}`
- Add an entry to a dictionary by defining a key and value `dict["key"] = "value"`
- Looping through a dictionary gives you the key
- You can use the key to access its corresponding value
- Key and index is how you access a list nested in a dictionary
- Nested lists within a list can be accessed by:
  1. Finding the index of the item in the first list
  2. Finding the index of the item needed from the second list
- `max()` can find the largest value
- `key=bids.get` tells `max()` to compare the dictionary values instead of the keys
- A variable can store the result of a function so it can be used later

---

## ⚠️ Things to Remember

- Key must match including capitalization or there will be a KeyError
- Dictionary keys are used to access their corresponding values
- `max(dictionary)` compares the keys by default
- `max(dictionary, key=dictionary.get)` compares the values
- Common bugs
  - Accidentally creating a new dictionary inside a loop
  - Forgetting that indentation determines what code belongs inside a loop or condition
- Keep dictionaries outside loops when you need to preserve the data between iterations

---

## 🚀 Key Takeaways

- Biggest lesson from today
  - Dictionaries allow me to connect related pieces of information using a key and value.

- Concept that finally "clicked"
  - `max(bids, key=bids.get)` — I learned that `key=` tells Python what information to use when deciding what is the "maximum."

- How this knowledge will help in future projects
  - I can use dictionaries to store and organize related data and use loops and built-in Python functions to analyze that data.