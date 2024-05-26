#Solution to https://platform.stratascratch.com/coding/2033-find-the-most-profitable-location?code_type=2

signups.head()
transactions.head()
import pandas as pd
df=pd.merge(signups,transactions,on='signup_id')
df['duration'] =  (df.signup_stop_date - df.signup_start_date).dt.days
df=pd.merge(df.groupby('location')['duration'].mean(),df,on='location')
df=pd.merge(df.groupby('location')['amt'].mean(),df,on='location')
df['ratio']=df['duration_x']/df['amt_x']
df[['location','duration_x','amt_x','ratio']].drop_duplicates().sort_values(by='ratio')
