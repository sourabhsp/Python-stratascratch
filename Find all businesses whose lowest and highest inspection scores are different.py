#Solution to https://platform.stratascratch.com/coding/9731-find-all-businesses-whose-lowest-and-highest-inspection-scores-are-different?code_type=2

sf_restaurant_health_violations.head()
sf_restaurant_health_violations.dropna(inplace=True)
import pandas as pd
df=pd.merge(sf_restaurant_health_violations.groupby('business_name')['inspection_score'].min().reset_index(),sf_restaurant_health_violations.groupby('business_name')['inspection_score'].max().reset_index(),on='business_name' )
df[df['inspection_score_x']==df['inspection_score_y']]