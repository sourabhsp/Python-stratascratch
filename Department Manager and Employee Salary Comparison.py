#Solution to https://platform.stratascratch.com/coding/2146-department-manager-and-employee-salary-comparison?code_type=2

import pandas as pd
employee_o.head()
employee_m=employee_o[employee_o.id!=employee_o.manager_id]
salary=employee_m.groupby('department')['salary'].mean()
merged1=pd.merge(employee_o,salary,on='department')
merged2=pd.merge(merged1,employee_o,left_on='manager_id',right_on='id')
merged2=merged2[merged2.id_x!=merged2.manager_id_x]
merged2[['department_x','id_x','salary_x','salary','salary_y']]

