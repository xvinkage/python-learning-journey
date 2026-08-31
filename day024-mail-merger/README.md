# Day 24 – Mail Merger

## 📚 Today's Concepts

- Reading files with `open()`
- `read()` vs `readline()` vs `readlines()`
- Working with lists of strings
- Using `for` loops to process multiple names
- String `.strip()`
- String `.replace()`
- Writing files with `open(..., mode="w")`
- Creating dynamic filenames with f-strings
- File paths and working directories

## 🛠️ What I Built

Built a **Mail Merger** program that:

- Reads a starting letter template
- Reads a list of invited names
- Loops through each name
- Removes the newline character from each name
- Replaces the `[name]` placeholder in the template
- Creates a personalized letter for each person
- Saves each letter into the `ReadyToSend` folder

## 💡 What I Learned

- `read()` reads the entire file as one string.
- `readline()` reads one line at a time.
- `readlines()` reads all lines and returns them as a list.
- `.strip()` removes unwanted whitespace such as the newline character `\n`.
- `.replace()` returns a new string rather than changing the original string.
- Files need to be opened in `"w"` mode when writing.
- Output files can be created inside a loop so each person gets their own file.
- f-strings can be used to dynamically create filenames.

## 🔑 Key Takeaways

The biggest lesson from this project was learning how to combine **file handling, loops, strings, and variables** to automate a repetitive task.

Instead of manually creating a letter for every person, Python can:

**Read → Process → Create → Save**

for as many names as are in the file.

## 🛠️ Skills Practiced

- Python
- File handling
- `open()`
- Reading and writing files
- Lists
- `for` loops
- String manipulation
- `.strip()`
- `.replace()`
- f-strings
- File paths
