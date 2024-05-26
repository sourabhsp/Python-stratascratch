#Solution to https://platform.stratascratch.com/coding/9606-differences-in-movie-ratings?code_type=2
import numpy as np

df = nominee_filmography[~nominee_filmography['rating'].isna()]
df = df[df.role_type == 'Normal Acting']
df['film_order'] = df.groupby(['name'])['id'].rank(ascending=False)
result = df[df['film_order']==2][['name', 'rating']].set_index('name')
result['lifetime_rating'] = df.groupby(['name'])['rating'].mean()
result['variance'] = abs(result['rating'] - result['lifetime_rating'])
result = result.reset_index()