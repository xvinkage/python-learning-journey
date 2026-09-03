# Day X – Beginner – Scope & Number Guessing Game

## 📚 Today's Concepts
- Local vs Global Scope
- Functions and scope
- Returning values from functions

---

## 🛠️ What I Built
- Prime number checker
- Number guessing game
  - Easy difficulty = 10 attempts
  - Hard difficulty = 5 attempts

---

## 💡 What I Learned
- Variables declared inside a function are local and aren't accessible outside that function (local scope).
- Variables declared outside of functions are global variables (global scope) and can be accessed inside functions.
- Scope applies to everything named (namespace), including functions nested inside other functions.
- Python does not have block scope like some other languages.
- Global constants are conventionally named in ALL CAPS.
- Functions can return values so the main program can use them instead of modifying global variables.
- Function parameters create local variables inside the function.

---

## ⚠️ Things to Remember
- Avoid using the same variable name for local and global variables because it can become confusing.
- You can access a global variable from inside a function without using `global` if you're only reading it.
- The `global` keyword is needed when you want to reassign a global variable inside a function.
- Avoid modifying global variables inside functions when possible; return a value instead.
- Keep functions responsible for one specific task.