# Solution to https://platform.stratascratch.com/coding/9917-average-salaries?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
employee.head()
employee.groupby('department')['salary'].mean()
df=pd.merge(employee,employee.groupby('department')['salary'].mean(), on='department' )[['department','first_name','salary_x','salary_y']]
df.rename(columns = {'salary_x':'salary','salary_y':'avg_salary'})