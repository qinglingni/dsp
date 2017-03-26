import pandas as pd
import re


# read csv file and rename the column names due to whitespace in names
df = pd.read_csv ('/users/qni/metis/faculty.csv',header = 0, sep=',', names = ['name','degree','title','email'])

#split degree columns because it contains multiple values in one column
df_degree = pd.DataFrame(df['degree'].str.split(expand=True).stack().rename('degree'))

# make sure the degree dataframe index is alinged with the original dataframe
df_degree.index = df_degree.index.droplevel(-1)

#clean up degree names becasue of special characters, and make them all upper case just in case
df_degree_c = df_degree['degree'].str.replace('[\W]+','').apply(lambda x: x.upper())

#join the cleaned up degree back to the original dataframe
df_n = df.drop('degree',axis=1).join(df_degree_c,how='left')
#print(df)
#print(df_n)


#title_count = df_n['title'].value_counts()
#print(title_count)

email_list = pd.DataFrame(df['email'].unique())
email_list.columns = ['email']
#print (email_list)

email_list.to_csv ('/Users/qni/metis/emails.csv',index=False)
"""
def find_domain (s):
    domain = re.findall ('@([^ ]*)',s)
    return domain

domain_list = df_n['email'].apply(lambda x : find_domain(x)[0]).unique()

#print (domain_list.unique())
"""
