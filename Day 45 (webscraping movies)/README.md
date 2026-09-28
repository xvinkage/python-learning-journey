# Day 45 – Intermediate – Web Scraping with Beautiful Soup

## 📚 Today's Concepts

- Web scraping with Beautiful Soup
- HTML parsing
- CSS selectors
- Extracting and processing data from webpages

---

## 🛠️ What I Built

- Scraped movie titles from a webpage using Beautiful Soup.
- Extracted HTML elements using CSS selectors.
- Stored the movie titles in a Python list.
- Reversed the list to put the movies in the required order.
- Wrote the movie titles to a text file using Python.

---

## 💡 What I Learned

- Beautiful Soup is a Python library used to parse HTML and XML and extract data from them.
- Web scraping is the process of automatically collecting information from webpages.
- CSS selectors can be used to find specific HTML elements.
- `.select()` can return multiple elements that match a CSS selector.
- `.getText()` / `.get_text()` can extract the text contained inside an HTML element.
- `robots.txt` tells automated crawlers which parts of a website the site owner requests they should or should not access.
- APIs are generally preferable when a website provides the data through an API because the data is structured specifically for programmatic use.
- Websites may use CAPTCHAs and other techniques to distinguish automated requests from human users.

---

## ⚠️ Things to Remember

- Beautiful Soup parses HTML; it does not fetch webpages by itself. Libraries such as `requests` can be used to retrieve the webpage.
- Always check a website's terms, `robots.txt`, and applicable laws before scraping.
- Publicly accessible data is not automatically free of copyright or other legal restrictions.
- Do not assume that publicly accessible information can always be reused however you want.
- Avoid sending excessive requests to a website.
- Adding delays and caching requests can reduce unnecessary traffic.
- An API should generally be used when an appropriate API is available.
- HTML structure can change, which can cause a scraper to stop working.

---

## 🚀 Key Takeaways

- I learned how Python can retrieve a webpage and use Beautiful Soup to turn the HTML into data I can work with.
- CSS selectors are a powerful way to target specific information within a webpage.
- Web scraping connects Python programming with real-world data.
- Scraping is useful when structured data is not available through an API, but it should be done responsibly.