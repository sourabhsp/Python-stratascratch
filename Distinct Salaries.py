#Solution to https://platform.stratascratch.com/coding/9898-unique-salaries?code_type=2

twitter_employee.head()
twitter_employee['rank']=twitter_employee.groupby('department')['salary'].rank(ascending=False)

twitter_employee[twitter_employee['rank']<=3][['department','salary']]