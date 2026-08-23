# Day X – Intermediate – Object Oriented Programming (OOP)

## 📚 Today's Concepts

- Object Oriented Programming (OOP)
- Why we use OOP
- Classes vs. objects
- Creating objects from classes
- Object attributes and methods
- Calling methods with objects
- Modifying object attributes
- Python packages and PyPI
- Using external packages

---

## 🛠️ What I Built / Practiced

- Practiced calling methods with Turtle
- Used the `prettytable` package
- Practiced modifying object attributes
- Practiced calling object methods
- Updated the Coffee Machine project to use OOP
- Worked with multiple classes interacting with each other (`Menu`, `MenuItem`, `CoffeeMaker`, `MoneyMachine`)

---

## 💡 What I Learned

- A **class** is a blueprint for creating objects.
- An **object** is an instance created from a class.
- Objects contain **attributes** (data) and **methods** (behavior).
- Use `object.attribute` to access or modify an object's data.
- Use `object.method()` to call behavior belonging to an object.
- A method can return an entire object, not just a simple value.
- `if object:` can be used to check whether an object was returned instead of `None`.
- PyPI is a repository where Python packages are published.
- External packages can add functionality without having to build everything yourself.
- OOP helps organize larger programs by grouping related data and behavior together.

---

## ⚠️ Things to Remember

- The **class** is the blueprint; the **object** is the thing created from that blueprint.
- Use PascalCase for class names.
- `object.attribute` accesses an object's data.
- `object.method()` calls an object's method.
- Create an object before using its instance methods.
- `self` refers to the current object.
- PyPI is a repository of Python packages.
- Don't assume a method returns the value you entered; check what it actually returns.
- Use `print()` and debugging to inspect objects when you're unsure what they contain.

---

## 🚀 Key Takeaways

- The biggest lesson today was understanding the difference between a **class and an object**.
- OOP started to click when I saw that `Menu` creates `MenuItem` objects and those objects contain their own attributes like `name`, `cost`, and `ingredients`.
- I learned that objects can interact with each other, which makes larger programs easier to organize.
- OOP will help me structure future projects into separate components instead of putting everything into one large file or collection of functions.

---

## 🧠 Skills Practiced

- Classes
- Objects
- Attributes
- Methods
- `self`
- Object interaction
- Python packages
- PyPI
- Importing modules
- Debugging objects
- Dictionaries
- Functions
- Loops
- User input

---

## 📂 Files

```text
main.py
menu.py
coffee_maker.py
money_machine.py