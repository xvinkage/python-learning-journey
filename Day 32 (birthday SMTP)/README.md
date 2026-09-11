# Day 32 – Intermediate – Send Email (smtplib) & Manage Dates (datetime)

## 📚 Today's Concepts

- SMTP (Simple Mail Transfer Protocol)
- `smtplib` for sending emails with Python
- `datetime` for working with dates and days of the week
- Environment variables with `.env` and `python-dotenv`
- Pandas DataFrames and converting them to dictionaries
- Reading and modifying text files
- f-strings and email subjects
- Returning values from functions
- Conditional logic based on dates

---

## 🛠️ What I Built

- **Birthday Wisher** — a program that checks a CSV file for birthdays matching today's date.
- Used `datetime` to determine the current month, day, and weekday.
- Used Pandas to read the birthday information from a CSV file.
- Converted the DataFrame into a list of dictionaries so I could loop through each person's information.
- Created a function to find birthdays and generate a personalized birthday letter.
- Randomly selected one of three letter templates.
- Replaced `[NAME]` in the template with the person's actual name.
- Used `smtplib` to connect to Gmail and send the personalized birthday email.
- Used environment variables to keep my email credentials out of the Python code.
- Added an email subject using the email message headers.
- Made the program send the email only when a birthday matches today's date.

---

## 💡 What I Learned

- `smtplib` allows Python to communicate with an SMTP server and send emails.
- `starttls()` secures the SMTP connection before logging in.
- `connection.login()` authenticates the email account.
- `connection.sendmail()` sends an email using a sender, recipient, and message.
- `connection.close()` closes the SMTP connection when finished.
- `datetime.datetime.now()` gets the current date and time.
- `.day`, `.month`, and `.weekday()` allow me to access parts of a date.
- `weekday()` returns `0` for Monday through `6` for Sunday.
- Environment variables can be loaded with `os.getenv()` and `python-dotenv`.
- `pd.read_csv()` can load CSV data into a DataFrame.
- `to_dict(orient="records")` converts a DataFrame into a list of dictionaries.
- When looping through a list of dictionaries, the loop variable represents the current dictionary.
- A function can use `return` to send a value back to the code that called it.
- `random.randint()` can be used to randomly select a letter template.
- `.replace()` can replace placeholder text such as `[NAME]`.
- An email subject can be added using the `Subject:` email header followed by `\n\n` to separate the header from the message body.
- I learned that `in` behaves differently with Pandas Series than I initially expected because it checks the Series index rather than its values.
- I learned that when working with a list of dictionaries, I need to access values through the current dictionary, such as `birthday["month"]` and `birthday["email"]`.

---

## ⚠️ Things to Remember

- Use `now.day` and `now.month` rather than `now.day()` and `now.month()` because they are attributes, not methods.
- `datetime.weekday()` returns numbers from `0` through `6`.
- Don't use my normal Gmail password directly in code. Use an appropriate Gmail App Password when SMTP authentication requires it.
- Never hard-code email passwords or other credentials into Python files.
- Keep `.env` out of GitHub and other public repositories.
- Close SMTP connections after sending with `connection.close()`.
- Check the date **before** connecting to the SMTP server if the program should only send emails on certain days.
- When using an f-string with dictionary keys, avoid conflicting quotation marks:
  `f'Hello {birthday["name"]}'`
- `return` exits the function, so returning from inside a loop stops the loop after the first matching birthday.
- If multiple people can have the same birthday, returning immediately means only the first matching person will receive an email.
- Keep functions focused on a specific task—for example, finding a birthday and creating the letter rather than mixing unrelated responsibilities.