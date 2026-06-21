##                            Sales Analytics Project 

An end-to-end Sales Analytics project built using **SQL, Python, and Power BI** to analyze business performance, identify profit drivers, and create interactive dashboards.

---

## Project Overview

This project analyzes the Sample Superstore dataset to answer important business questions such as:

* Which category generates the highest sales?
* Which category generates the highest profit?
* How do discounts affect profitability?
* What are the sales trends over time?
* Which regions and customer segments perform best?

The project combines:

* **SQL** for business queries
* **Python (Pandas, Matplotlib, Seaborn)** for EDA and visualization
* **Power BI** for interactive dashboards

---

## Tools Used

* Python 3.13
* Pandas
* Matplotlib
* Seaborn
* MySQL
* Power BI
* VS Code
* Git & GitHub

---

## Project Structure

```text
sales-analytics-project

├── data
│   └── superstore.csv

├── sql
│   └── business_queries.sql

├── python
│   ├── eda.py
│   └── visualize.py

├── powerbi
│   └── SalesDashboard.pbix

├── outputs
│   ├── sales_by_category.png
│   ├── profit_by_category.png
│   ├── correlation.png
│   └── sales_trend.png

└── README.md
```

---

## SQL Analysis

Performed business analysis using SQL queries:

* Total sales by region
* Total profit by category
* Profitability of furniture sub-categories
* Average discount analysis
* Identified loss-making products

### Key Finding

Furniture generated high sales but lower profits.

Further analysis showed:

* Tables and Bookcases produced negative profits.
* Higher discounts were associated with lower profitability.

---

## Python EDA

Performed:

* Dataset overview
* Shape and column inspection
* Missing value analysis
* Statistical summary
* Category-wise sales and profit analysis
* Correlation analysis

### Correlation Findings

* Sales and Profit showed a positive relationship.
* Discount and Profit showed a negative relationship.
* Higher discounts generally reduced profitability.

---

## Visualizations

Generated and saved:

* Sales by Category
* Profit by Category
* Correlation Heatmap
* Monthly Sales Trend

All visualizations are available in the `outputs/` folder.

---

## Power BI Dashboard

Created an interactive dashboard containing:

* KPI Cards

  * Total Sales
  * Total Profit
  * Profit Margin

* Sales Trend

* Sales by Category

* Profit by Category

* Interactive slicers

  * Region
  * Segment
  * Category

---

## Key Insights

* Technology generated the highest sales and profit.
* Furniture generated strong sales but lower profits.
* Tables and Bookcases were the major loss-making products.
* Discounts negatively impacted profitability.
* Sales showed an overall increasing trend over time.

---

## Future Improvements

* Predict sales and profit using Machine Learning.
* Add customer segmentation analysis.
* Deploy dashboard online using Power BI Service.

---

