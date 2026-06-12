# FMCG Sales Performance Analysis (2023–2025)

## What This Project Is About

Most FMCG businesses sit on mountains of sales data but struggle to answer basic questions — which regions are actually profitable, which products are worth pushing, and are our promotions doing anything useful? This project digs into 3 years of global FMCG sales data across 17 countries and 5 regions to answer exactly those questions.

The goal wasn't just to build a dashboard. It was to find insights that a sales manager or regional director could actually act on.

---

## Tools & Technologies

- **PostgreSQL** — data storage and querying
- **Python** (pandas, sqlalchemy, matplotlib, seaborn) — data analysis and visualisation
- **Power BI** — interactive dashboard
- **VS Code** — development environment

---

## Dataset Overview

| Property | Detail |
|---|---|
| Rows | 18,240 orders |
| Columns | 27 |
| Date Range | January 2023 – December 2025 |
| Regions | 5 (Europe, North America, Asia, South America, Oceania) |
| Countries | 17 |
| Brands | 17 |
| SKUs | 30 |
| Total Revenue | $14.45M |
| Total Profit | $3.31M |

---

## Business Questions Answered

1. Which region is most profitable — and is it consistent year on year?
2. Which product category drives the most revenue, and which is most efficient?
3. How has sales revenue grown year on year?
4. Which countries deliver the best profit margins?
5. Are promotions actually working, or are discounts eating into margins?

---

## Key Insights

**Regional Profitability**
Europe leads with $1.13M profit — 34% of total global profit. But Oceania and South America are significantly behind, suggesting untapped potential or operational inefficiencies in those markets.

**Category Performance**
Beverages generates the highest revenue ($3.74M) but Household products have a superior profit margin. More volume doesn't always mean more profit — Household squeezes more value out of every dollar of revenue.

**Sales Growth**
Revenue has grown consistently from $4.59M in 2023 to $5.02M in 2025. However growth is decelerating — 5.4% in 2024 dropping to 3.6% in 2025. Worth monitoring.

**Country Efficiency**
Brazil has a higher profit margin (24.35%) than the USA (23.52%) despite significantly lower revenue. If Brazil can scale, it could become a high-value market.

**Promotions**
No-Promo orders generated 3x more profit than any promoted campaign ($1.43M vs next best $487K). Loyalty Cashback delivered the best ROI among promotions at 308% with the lowest marketing spend. Heavy discount promotions like Introductory Offers and Festival Campaigns are underperforming.

**Seasonal Pattern**
Europe consistently dips in Q2 every year. A targeted Q2 campaign could close this recurring gap.

---

## Dashboard Preview

![FMCG Dashboard](output/dashboard_preview.png)

---

## Project Structure

```
fmcg_sales_project/
│
├── src/
│   ├── db.py              # database connection
│   ├── eda.py             # exploratory data analysis
│   ├── analysis.py        # business questions analysis
│   └── visualise.py       # Python charts
│
├── output/                # saved charts and exports
│
└── README.md
```

---

## How to Run

1. Clone the repository
2. Set up PostgreSQL and create a database called `fmcg_sales`
3. Load the CSV into PostgreSQL using pgAdmin Import
4. Create a virtual environment and install dependencies:

```bash
pip install psycopg2-binary pandas sqlalchemy matplotlib seaborn numpy
```

5. Update the connection string in `db.py` with your credentials
6. Run scripts in order:

```bash
python src/eda.py
python src/analysis.py
python src/visualise.py
```

7. Open `fmcg_sales_dashboard.pbix` in Power BI Desktop

---

## About Me

Career switcher from retail management (Domino's Store Manager) into data analytics. MSc Applied Data Science, University of Central Lancashire. PL-300 Power BI certified.

This project combines my retail domain knowledge with technical data skills — I know what these numbers mean from both sides of the counter.

[GitHub](https://github.com/Mahesh521)
