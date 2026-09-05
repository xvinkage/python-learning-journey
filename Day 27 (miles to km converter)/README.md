# Day 27 – Intermediate – Graphical User Interfaces with Tkinter and Function Arguments

## 📚 Today's Concepts

- Tkinter
- Graphical User Interfaces (GUIs)
- Widgets
- `pack()`, `place()`, and `grid()` layout managers
- Function arguments
- Default/optional arguments
- Unlimited positional arguments: `*args`
- Unlimited keyword arguments: `**kwargs`

---

## 🛠️ What I Built

### 🧮 Miles to Kilometers Converter

Built a simple GUI application that:

- Uses Tkinter to create a graphical interface
- Allows the user to enter a number of miles
- Converts miles to kilometers
- Rounds the result to two decimal places
- Updates the result dynamically when the Calculate button is pressed
- Uses `grid()` to organize the widgets

### 📐 Tkinter Layout Managers

Learned that Tkinter provides different ways to position widgets:

- `pack()` – organizes widgets based on available space
- `place()` – positions widgets using specific coordinates
- `grid()` – organizes widgets into rows and columns

---

## 💡 What I Learned

- Tkinter is a Python library commonly used to create graphical user interfaces.
- GUI programs are event-driven: something like clicking a button can trigger a function.
- Functions can accept arguments to make them more flexible.
- Arguments can have default values.

```python
def function(a=1, b=2):
    pass
```

If no values are supplied, the defaults are used.

- `*args` allows a function to accept an unlimited number of positional arguments.

```python
def add(*args):
    for number in args:
        print(number)
```

- `**kwargs` allows a function to accept an unlimited number of keyword arguments.
- `kwargs` is treated like a dictionary containing the keyword arguments.

```python
def function(**kwargs):
    print(kwargs)
```

- `**kwargs` can be useful when creating classes or functions that have optional attributes or settings.

---

## ⚠️ Things to Remember

- Default arguments are used when no value is provided.

```python
def function(a=1, b=2):
    pass
```

- Required arguments still need to be provided unless they have default values.
- You only need to provide an argument when you want to override its default value.
- `*args` collects positional arguments and can be looped through.
- `**kwargs` collects keyword arguments into a dictionary.
- `args` behaves like a tuple.
- `kwargs` behaves like a dictionary.
- When passing a function to Tkinter's `command`, don't call the function immediately:

```python
command=calc_km
```

rather than:

```python
command=calc_km()
```

---

## 🚀 Key Takeaways

- I learned how Python can be used to create actual graphical applications instead of only command-line programs.
- The biggest practical lesson was connecting a button to a function and using that function to retrieve user input, perform a calculation, and update the GUI.
- I learned that function arguments make code more flexible and reusable.
- `*args` and `**kwargs` allow functions and classes to handle an unknown number of arguments.
- Understanding `**kwargs` will be especially useful when working with libraries and classes that have many optional settings.
- Tkinter gives me another way to turn Python programs into tools that other people can actually interact with.

---