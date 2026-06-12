import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from db import engine
import numpy as np

query = """SELECT * FROM fmcg_sales;"""

df=pd.read_sql(query,engine)

print(df.shape)

sns.set_theme(style='whitegrid')

regional_profit= df.groupby('region')['profit_usd'].sum().reset_index().sort_values('profit_usd',ascending=False)

plt.figure(figsize=(10,6))
sns.barplot(data=regional_profit,x='region',y='profit_usd')
plt.title("Regional Profit")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.tight_layout()
plt.gca().yaxis.set_major_formatter(
    plt.FuncFormatter(lambda x, _: f'${x/1_000_000:.1f}M')
)
import os

output_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'output')
plt.savefig(os.path.join(output_path, 'regional_profit.png'), dpi=150, bbox_inches='tight')
plt.show()

Yearly_Quarterly_Sales= df.groupby(['year','quarter'])['net_revenue_usd'].sum().reset_index()
Yearly_Quarterly_Sales['Period']=Yearly_Quarterly_Sales['year'].astype(str)+ ' '+Yearly_Quarterly_Sales['quarter'].astype(str)
plt.figure(figsize=(10,6))
sns.lineplot(data=Yearly_Quarterly_Sales,x='Period',y='net_revenue_usd')
plt.title("Yearly Sales Growth")
plt.xlabel("Period")
plt.ylabel("Net_Revenue")
plt.tight_layout()
plt.gca().yaxis.set_major_formatter(
    plt.FuncFormatter(lambda x, _: f'${x/1_000_000:.1f}M')
)
x_numeric=range(len(Yearly_Quarterly_Sales))
z=np.polyfit(x_numeric,Yearly_Quarterly_Sales['net_revenue_usd'],1)
p=np.poly1d(z)
plt.plot(Yearly_Quarterly_Sales['Period'],p(x_numeric),color='red',linestyle='--',linewidth=2,label='Trend')
plt.legend()
output_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'output')
plt.savefig(os.path.join(output_path, 'yearly_sales_growth.png'), dpi=150, bbox_inches='tight')
plt.show()

# Catergory Revenue & Profit Comparision
category_revenue=df.groupby('product_category').agg(
    Net_Sales=('net_revenue_usd','sum'),
    Net_Profit=('profit_usd','sum')
).reset_index()
category_revenue.columns=['Category','Net_Sales','Net_Profit']
category_melted= category_revenue.melt(
    id_vars='Category',
    value_vars=['Net_Sales','Net_Profit'],
    var_name='Metric',
    value_name='Revenue vs Profit'
)
print(category_melted)
category_revenue=category_revenue.sort_values('Net_Sales',ascending=False)

plt.figure(figsize=(12,6))
sns.barplot(data=category_melted,x='Category',y='Revenue vs Profit',hue='Metric',order=category_revenue['Category'])
plt.title("Category Revenue and Profit Comparision")
plt.xlabel("Category")
plt.ylabel("Revenue vs Profit")
plt.tight_layout()
plt.gca().yaxis.set_major_formatter(
    plt.FuncFormatter(lambda x, _: f'${x/1_000_000:.1f}M')
)
output_path=os.path.join(os.path.dirname(os.path.dirname(__file__)),'output')
plt.savefig(os.path.join(output_path,'category_revenue_profit.png'), dpi=150,bbox_inches='tight')
plt.show()