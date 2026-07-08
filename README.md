# Sales Performance Dashboard - Tableau Project

## Project Overview

This project focuses on analyzing sales data to identify revenue trends, product performance, and customer sales insights using Tableau.

The objective of this project is to transform raw CSV data into interactive visualizations and dashboards that help businesses understand sales performance and make data-driven decisions.

---

## Tools & Technologies Used

- Tableau Desktop
- CSV Data Sources
- Data Visualization
- Data Analysis
- Git & GitHub

---

## Project Structure

```text
data-engineering-project
│
├── data
│   ├── sales_summary.csv
│   ├── product_performance.csv
│   ├── customer_sales.csv
│   ├── raw
│   └── processed
│
├── Tableau
│   └── Sales_Performance_Dashboard.twb
│
├── Images
│   └── Sales Analysis Dashboard.png
│
├── src
│   ├── ingestion.py
│   ├── transformation.py
│   ├── data_quality.py
│   └── run_pipeline.py
│
├── sql
│   └── analytics.sql
│
├── config
│   └── config.py
│
├── reports
│
├── requirements.txt
│
└── README.md       

---

## Dataset Description

### sales_summary.csv

**Purpose:**
- Provides summarized sales information by category.

**Used For:**
- Revenue analysis by category.

**Visualization:**
- Revenue by Category Bar Chart

---

### product_performance.csv

**Purpose:**
- Contains product-level sales performance data.

**Used For:**
- Comparing product sales and identifying high-performing products.

**Visualization:**
- Product Performance Analysis Chart

---

### customer_sales.csv

**Purpose:**
- Contains customer-level sales information.

**Used For:**
- Understanding customer purchase patterns.

**Visualization:**
- Customer Sales Analysis Chart

---

## Dashboard Features

The Tableau dashboard provides:

- Revenue analysis by category
- Product performance comparison
- Customer sales analysis
- Interactive dashboard filtering
- Business-focused visualizations

## Dashboard Preview

![Sales Performance Dashboard](Images/Sales%20Analysis%20Dashboard.png)

---

## Tableau Dashboard Sheets

### Sheet 1: Revenue Analysis
- Data Source: sales_summary.csv
- Chart: Bar Chart
- Purpose: Analyze revenue distribution across categories

### Sheet 2: Product Performance
- Data Source: product_performance.csv
- Chart: Bar Chart
- Purpose: Compare product sales performance

### Sheet 3: Customer Sales Analysis
- Data Source: customer_sales.csv
- Chart: Customer Sales Visualization
- Purpose: Analyze customer sales contribution

---

## Key Insights

- Analyzed sales performance across different categories.
- Identified product-level sales trends.
- Evaluated customer sales patterns.
- Created an interactive Tableau dashboard for reporting and analysis.

---

## Future Improvements

- Connect dashboard to a live database.
- Automate data refresh using ETL pipelines.
- Add advanced analytics and forecasting models.
- Integrate cloud data storage solutions.

---

## Author

**Anitha Raj Bale**

Data Analytics / Data Engineering Portfolio Project
