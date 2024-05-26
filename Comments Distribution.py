#Solution to https://platform.stratascratch.com/coding/10297-comments-distribution?code_type=1

import pandas as pd
fb_users.head()
fb_comments.head()

#Creating a merged dataframe df
df = pd.merge(fb_users, fb_comments, left_on=['id'], right_on=['user_id'])
df = df[df['created_at'] >= df['joined_at']]
df=df[(df.joined_at.dt.year>=2018) & (df.joined_at.dt.year<=2020)]
df= df[(df.created_at.dt.month==1)&(df.created_at.dt.year==2020)]
df1=df.groupby('id')['user_id'].count().reset_index()
df1.groupby('user_id')['id'].count()
