#Solution to https://platform.stratascratch.com/coding/10172-best-selling-item?code_type=1

# Import your libraries
import pandas as pd

# Start writing code
online_retail.head()
online_retail['month']=online_retail['invoicedate'].dt.month
online_retail['total_paid']=online_retail['quantity']*online_retail['unitprice']
online_retail.head()
df=online_retail.groupby(['month'])['total_paid'].max()
pd.merge(df,online_retail,on=['month','total_paid'])[['month','description','total_paid']]

