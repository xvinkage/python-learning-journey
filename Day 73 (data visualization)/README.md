# Day 73 – Data Analysis with Pandas & Data Visualization

## 1. Grouping Data

Used `.groupby()` to explore the number of posts and entries per programming language.

- Groups records based on a specific category.
- Helps summarize and compare data across different groups.

## 2. Working with Dates

Converted strings into Datetime objects using `pd.to_datetime()` for easier date handling and plotting.

```python
df['Date'] = pd.to_datetime(df['Date'])
```

- Converts date strings into a format Pandas can recognize.
- Makes it easier to sort, analyze, and visualize time-series data.

## 3. Reshaping a DataFrame

Used `.pivot()` to reshape a DataFrame by converting categories into columns.

```python
df.pivot(index='Date', columns='Language', values='Posts')
```

- `index` determines the rows.
- `columns` determines which categories become new columns.
- `values` determines what data fills the table.

## 4. Finding and Handling Missing Values

Used `.count()` and `isna().values.any()` to look for missing (`NaN`) values.

```python
df.count()
df.isna().values.any()
```

Replaced missing values using `.fillna()`.

```python
df.fillna(0)
```

- `.count()` counts non-missing values in each column.
- `.isna()` identifies missing values.
- `.values.any()` checks whether any missing values exist.
- `.fillna()` replaces missing values with a specified value.

## 5. Creating Line Charts

Used `.plot()` to create multiple line charts with a `for` loop.

```python
df.plot()
```

- `.plot()` creates visualizations directly from a DataFrame.
- A `for` loop can automate the creation of multiple charts.

## 6. Styling Charts

Customized charts by changing:

- Chart size.
- Axis labels.
- Upper and lower axis bounds.
- Legends.

Added a legend to distinguish between different lines using their colors.

## 7. Smoothing Time-Series Data

Used `.rolling().mean()` to calculate rolling averages and smooth out time-series observations.

```python
df.rolling(window=30).mean()
```

- Calculates the average over a moving window of observations.
- Helps reduce short-term fluctuations.
- Makes longer-term trends easier to identify.

---

## Quick Reference

| Method / Function | Purpose |
|---|---|
| `.groupby()` | Group data by category |
| `pd.to_datetime()` | Convert strings to dates |
| `.pivot()` | Reshape a DataFrame |
| `.count()` | Count non-missing values |
| `.isna()` | Identify missing values |
| `.values.any()` | Check if any values are True |
| `.fillna()` | Replace missing values |
| `.plot()` | Create charts |
| `.rolling()` | Create a rolling window |
| `.mean()` | Calculate an average |

## Key Takeaway

Pandas can do more than organize and manipulate data. Combined with visualization, it can help identify patterns, compare categories, and reveal trends over time.