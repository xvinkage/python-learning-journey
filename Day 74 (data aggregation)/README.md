# Data Analysis – Pandas, Matplotlib & Relational Databases

## 1. Markdown in Jupyter Notebooks

Use Markdown to organize and document notebooks.

- `#` – Main heading
- `##` – Subheading
- `###` – Smaller heading

You can also embed images using HTML:

```html
<img src="image-url" />
```

## 2. Aggregating Data

Combine `.groupby()` and `.count()` to aggregate data by category.

```python
df.groupby('Category').count()
```

Use `.value_counts()` to count how frequently individual values appear in a column.

```python
df['Category'].value_counts()
```

## 3. Slicing DataFrames

Use square bracket notation to select a range of rows.

```python
df[:-2]   # All rows except the last two
df[:10]   # First ten rows
```

## 4. Aggregating with .agg()

Use `.agg()` to perform an operation on a particular column or grouped data.

```python
df.agg({'Sales': 'sum'})
```

Other possible operations include:
- `sum`
- `mean`
- `min`
- `max`
- `count`

## 5. Renaming Columns

Use `.rename()` to change DataFrame column names.

```python
df.rename(columns={'old_name': 'new_name'})
```

## 6. Visualizing Data with Matplotlib

### Line Charts with Two Axes

Create a line chart with two separate Y-axes to visualize data with different scales.

This is useful when comparing two measurements that have very different ranges.

### Scatter Plots

Use Matplotlib to create scatter plots and visualize relationships between two variables.

```python
import matplotlib.pyplot as plt

plt.scatter(x_values, y_values)
plt.show()
```

### Bar Charts

Use Matplotlib to create bar charts for comparing values across categories.

```python
plt.bar(categories, values)
plt.show()
```

## 7. Relational Databases

Work with tables in a relational database using:

- **Primary keys:** Uniquely identify each record in a table.
- **Foreign keys:** Reference primary keys in another table to establish relationships.

## 8. Merging DataFrames

Use `.merge()` to combine DataFrames based on a shared column.

```python
merged_df = df1.merge(df2, on='id')
```

This is similar to joining tables in a relational database.

---

## Quick Reference

| Method / Function | Purpose |
|---|---|
| Markdown `#` | Create notebook headings |
| HTML `<img>` | Embed images |
| `.groupby()` | Group records by category |
| `.count()` | Count non-missing values |
| `.value_counts()` | Count occurrences of unique values |
| `df[:-2]` | Exclude last two rows |
| `df[:10]` | Select first ten rows |
| `.agg()` | Apply aggregation operations |
| `.rename()` | Rename columns |
| `plt.scatter()` | Create scatter plots |
| `plt.bar()` | Create bar charts |
| `plt.twinx()` | Create a second Y-axis |
| Primary key | Uniquely identify a record |
| Foreign key | Link related tables |
| `.merge()` | Combine DataFrames |

## Key Takeaway

Pandas and Matplotlib allow you to manipulate, aggregate, combine, and visualize data. Relational database concepts provide a foundation for working with structured data across multiple tables.