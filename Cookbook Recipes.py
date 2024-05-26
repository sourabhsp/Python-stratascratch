#Solution to https://platform.stratascratch.com/coding/2089-cookbook-recipes?code_type=2
import pandas as pd

cookbook_titles.head()
maximum=cookbook_titles.page_number.max()
dct={'left_page_number':[],'left_title':[],'right_title':[]}
for i in range(0,round(maximum/2)):
    dct['left_page_number'].append(2*i)
    temp1=cookbook_titles.loc[cookbook_titles['page_number']==2*i].title.values
    if not temp1:
        dct['left_title'].append('')
    else:
        dct['left_title'].append(temp1[0])
    temp2=cookbook_titles.loc[cookbook_titles['page_number']==2*i+1].title.values
    if not temp2:
        dct['right_title'].append('')
    else:
        dct['right_title'].append(temp2[0])
    
pd.DataFrame(dct)

    