# Day 72 – Data Analysis with Pandas

## Exploring a DataFrame

Use `.head()`, `.tail()`, `.shape` and `.columns` to explore your DataFrame and find out the number of rows and columns as well as the column names.

## Handling Missing Data

Look for NaN (Not a Number) values with `.isna()` and consider using `.dropna()` to clean up your DataFrame.

## Accessing Data

You can access entire columns of a DataFrame using square bracket notation:

```python
df['column name']
df[['column name 1', 'column name 2', 'column name 3']]
```

You can access individual cells in a DataFrame by chaining square brackets:

```python
df['column name'][index]
```

Or using `.loc[]`:

```python
df['column name'].loc[index]
```

## Finding Maximum and Minimum Values

The largest and smallest values, as well as their positions, can be found with:

- `.max()`
- `.min()`
- `.idxmax()`
- `.idxmin()`

## Sorting and Adding Columns

You can sort the DataFrame with `.sort_values()` and add new columns with `.insert()`.

## Grouping Data

To create an Excel-style Pivot Table by grouping entries that belong to a particular category, use the `.groupby()` method.

---

## Quick Reference

| Method / Attribute | Purpose |
|---|---|
| `.head()` | First rows |
| `.tail()` | Last rows |
| `.shape` | Rows and columns |
| `.columns` | Column names |
| `.isna()` | Find missing values |
| `.dropna()` | Remove missing values |
| `.loc[]` | Access by index label |
| `.iloc[]` | Access by position |
| `.max()` / `.min()` | Largest / smallest value |
| `.idxmax()` / `.idxmin()` | Index of largest / smallest |
| `.sort_values()` | Sort data |
| `.insert()` | Insert a column |
| `.groupby()` | Group and aggregate data |