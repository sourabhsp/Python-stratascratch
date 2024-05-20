# Solution to question : https://platform.stratascratch.com/coding/10350-algorithm-performance?code_type=2 


import pandas as pd

fb_search_events.head()
fb_search_events['ratings']=0
for i in range(0,len(fb_search_events.index)):
    if fb_search_events['clicked'][i]==0:
        fb_search_events['ratings'][i]=1
    elif (fb_search_events['clicked'][i]==1) & (fb_search_events['search_results_position'][i]>3):
        fb_search_events['ratings'][i]=2
    else: 
        fb_search_events['ratings'][i]=3
result = fb_search_events.groupby('search_id')['ratings'].max()