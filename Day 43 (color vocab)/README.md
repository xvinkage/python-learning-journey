# Day 43 – Intermediate – Web Foundation – Introduction to CSS

## 📚 Today's Concepts

- CSS — Cascading Style Sheets
- CSS selectors
- Classes and IDs
- Attribute selectors
- Inline, internal, and external CSS

---

## 🛠️ What I Built

- Styled the Spanish vocabulary webpage using CSS.
- Used ID selectors to give each Spanish color its appropriate color.
- Used an element selector to change the font weight of the headings.
- Used CSS to set all images to 200px by 200px.
- Linked an external CSS file to the HTML document.

---

## 💡 What I Learned

- CSS stands for Cascading Style Sheets.
- A CSS selector selects HTML elements to which CSS rules should be applied.
- A class selector is indicated by a `.` and can be used to group multiple elements.
- A class is an HTML attribute used to identify a group of elements.
- An ID selector is indicated by `#`.
- An ID is an HTML attribute used to identify a specific element.
- An ID should be unique within a single HTML document.
- An attribute selector can target elements based on their attributes, for example:
  `element[attribute] { color: red; }`

---

## ⚠️ Things to Remember

- CSS controls the presentation and styling of a website.
- There are three common ways to add CSS:
  - Inline CSS
  - Internal CSS
  - External CSS
- Inline CSS is written directly inside an HTML element using the `style` attribute:
  `style="property: value;"`
- Internal CSS is written inside a `<style>` element:
  `selector { property: value; }`
- External CSS is written in a separate `.css` file and connected to the HTML using:
  `<link rel="stylesheet" href="./styles.css">`
- External CSS is generally preferred for larger projects because it keeps the styling separate from the HTML structure.

---

## 🚀 Key Takeaways

- CSS allows me to control how HTML content looks without changing the HTML structure.
- Selectors determine which HTML elements receive a CSS rule.
- Classes are useful when multiple elements need the same styling.
- IDs can target a specific unique element.
- Separating HTML structure from CSS styling will make larger projects easier to organize and maintain.