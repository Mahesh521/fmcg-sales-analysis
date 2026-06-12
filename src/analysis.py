import psycopg2
import pandas as pd
from db import engine

query = """SELECT * FROM fmcg_sales;"""

df = pd.read_sql(query, engine)
print(df.shape)

#Q1: Regional Profitability
regional_quarterly_profit = df.groupby(['region','year','quarter'])['profit_usd'].sum().reset_index()
regional_quarterly_profit.columns=['Region','Year','Quarter','Total_Profit']
regional_quarterly_profit = regional_quarterly_profit.sort_values('Total_Profit',ascending=False)

print("Q1 - Regional Profitability:")
print(regional_quarterly_profit)

# Q2: Category Revenue
category_revenue= df.groupby('product_category').agg(Revenue=('net_revenue_usd','sum'),Units_Sold=('units_sold','sum'), Net_Profit=('profit_usd','sum')).reset_index()
category_revenue.columns = ['Category','Revenue','Units Sold','Net_Profit']
category_revenue = category_revenue.sort_values('Revenue', ascending=False)
print("Q2: Categorical Revenue:")
print(category_revenue)

#Q3: Year On Year Growth

yearly_sales = df.groupby('year').agg(
   Net_Sales=('net_revenue_usd','sum'),
   Net_Profit=('profit_usd','sum')
).reset_index()
yearly_sales.columns=['Year','Net_Sales','Net_Profit']
yearly_sales.sort_values('Net_Sales',ascending=False)

yearly_sales['Yoy_Growth_%']= round(yearly_sales['Net_Sales'].pct_change()*100,2)
print("Q3: Year on Year Growth")
print(yearly_sales)
# which country or region gives more sales and profit

country_performace= df.groupby(['region','country']).agg(
    Net_Sales=('net_revenue_usd','sum'),
    Net_Profit = ('profit_usd','sum')
).reset_index().sort_values('Net_Sales',ascending=False)
country_performace.columns=['Region','Country','Net_Sales','Net_Profit']
country_performace['Profit_Margin_%']=round((country_performace['Net_Profit']/country_performace['Net_Sales'])*100,2)
print(country_performace)

# Promotion 

promotion_analysis = df.groupby('promotion_type').agg(
    Marketing_spend=('marketing_spend_usd','sum'),
    Net_Profit=('profit_usd','sum'),
    AVG_Discount=('discount_pct','mean')
).reset_index().sort_values('Net_Profit', ascending=False)
promotion_analysis['AVG_Discount']=promotion_analysis['AVG_Discount'].round(2)
promotion_analysis['ROI']=round((promotion_analysis['Net_Profit']/promotion_analysis['Marketing_spend'])*100,2)
print(promotion_analysis)