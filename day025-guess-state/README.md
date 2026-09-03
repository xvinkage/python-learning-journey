# Day 25 – Intermediate – Working with CSV Data and the Pandas Library

## 📚 Today's Concepts

- Working with CSV files using Python
- Using the Pandas library to read and analyze CSV data
- Understanding Pandas Series and DataFrames
- Converting a Pandas Series into a Python list
- Filtering a DataFrame to find specific data
- Extracting individual values from a DataFrame using `.iloc`
- Creating new DataFrames from Python lists
- Exporting DataFrames to CSV files

---

## 🛠️ What I Built

### 🐿️ Squirrel Census Data Project

Analyzed the Central Park Squirrel Census CSV data using Pandas.

- Read a CSV file into a Pandas DataFrame
- Selected the `Primary Fur Color` column
- Converted the column into a Python list
- Counted the number of squirrels with Gray, Cinnamon, and Black fur
- Created a new DataFrame containing the fur colors and their counts
- Exported the results into a new CSV file

### 🗺️ U.S. States Game

Created an interactive game using Turtle and Pandas.

- Displayed a blank map of the United States
- Loaded state names and their coordinates from a CSV file
- Asked the user to guess U.S. states
- Checked whether the guessed state existed in the DataFrame
- Filtered the DataFrame to find the correct state's coordinates
- Created a new Turtle to write each correctly guessed state on the map
- Stored correctly guessed states in a list
- Prevented the score from increasing when states were guessed more than once
- Allowed the user to type `Exit` to leave the game
- Generated a `states_to_learn.csv` file containing states that were not guessed

---

## 💡 What I Learned

- Pandas can easily read CSV files using `pd.read_csv()`
- A DataFrame is similar to a table with rows and columns
- A Series represents a single column of data
- Pandas makes working with large amounts of structured data much easier
- A Series can be converted into a Python list using `.to_list()` or `.tolist()`
- DataFrames can be filtered to find specific rows

For example, filtering a DataFrame based on a state name:

`df[df["state"] == answer_state]`

- `.iloc[0]` can be used to retrieve an individual value from a filtered Series
- A Python list can be converted into a DataFrame
- DataFrames can be exported into CSV files using `.to_csv()`
- Column names can be assigned when creating a DataFrame

---

## ⚠️ Things to Remember

- A Pandas Series is similar to a one-dimensional collection of values, but it is not exactly the same thing as a normal Python list
- Use `.to_list()` or `.tolist()` when you specifically need a Python list
- Pandas makes calculations such as averages, counts, minimums, maximums, and standard deviations much easier
- When filtering a DataFrame, the result may still be a DataFrame even if only one row is found
- Use `.iloc[0]` to extract a single value when appropriate


---

## 🚀 Key Takeaways

- Pandas is much more powerful than manually reading CSV data when working with structured datasets
- I learned how to move between CSV data, Pandas DataFrames, Series, and regular Python lists
- Filtering a DataFrame allows me to connect user input with related data such as coordinates
- Pandas can be used not only for analyzing data but also for generating new datasets and CSV files
- The U.S. States Game showed me how Pandas can work together with other Python libraries like Turtle
- These skills can be applied to future projects involving automation, business data, reporting, data cleaning, and data-driven applications

---