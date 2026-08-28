# Day  – Intermediate – Build the Snake Game Part 2: Inheritance & List Slicing

## 📚 Today's Concepts

- Class inheritance
- Using `super().__init__()`
- List slicing
- Working with objects and inherited methods

---

## 🛠️ What I Built

- Completed the Snake game
- Added food and score functionality
- Added wall and tail collision detection
- Added keyboard controls for the snake
- Created separate `Snake`, `Food`, and `ScoreBoard` classes

---

## 💡 What I Learned

- Classes can inherit methods and attributes from another class.
- `Food(Turtle)` means the `Food` class inherits functionality from the `Turtle` class.
- `super().__init__()` initializes the parent class.
- Objects can contain other objects, such as the `Snake` containing a list of Turtle segments.
- List slicing is a way to take a portion of a list.
- Slicing works with lists and tuples.
- Slicing uses indexes to select the elements you want.
- `snake.snake_body[1:]` gets everything in the list starting at index `1`, which allowed me to check the snake's body without checking the head against itself.
- Methods should handle the behavior of the object they belong to.

---

## ⚠️ Things to Remember

- Inheritance allows a class to reuse attributes and methods from another class.
- Use `super().__init__()` when the child class needs to initialize the parent class.
- `class Food(Turtle)` means Food is a type of Turtle and gets Turtle's functionality.
- `object.attribute` accesses data stored in an object.
- `object.method()` calls behavior belonging to an object.
- List indexes start at `0`.
- `list[1:]` means start at index `1` and take everything after it.
- Be careful when creating new objects because they start with their default values/positions.
- Keep related data and behavior together inside their class when possible.