#Solution to https://platform.stratascratch.com/coding/10171-find-the-genre-of-the-person-with-the-most-number-of-oscar-winnings?code_type=2

oscar_nominees.head()
oscar_nominees=oscar_nominees[oscar_nominees['winner']==True]
oscar_nominees.groupby('nominee').size().to_frame('wins').reset_index()
import pandas as pd
df=pd.merge(oscar_nominees.groupby('nominee').size().to_frame('wins').reset_index(),nominee_information,
left_on='nominee',right_on='name')
df[df.wins==df.wins.max()].sort_values(by='nominee').head(1)[['top_genre']]



