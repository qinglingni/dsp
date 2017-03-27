import pandas as pd

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

def last_name(s):
    ln = s[s.rfind(' ')+1:len(s)]
    return ln

def first_name(s):
    fn = s[0:s.rfind(' ')]
    return fn

df_ln = pd.DataFrame(df['name'].apply(lambda x: last_name(x)).rename('lastname'))
df_fn = pd.DataFrame(df['name'].apply(lambda x: first_name(x)).rename('firstname'))
df_name = df_fn.join(df_ln,how='inner')
df_revised = df.join(df_name,how='inner').drop('name',axis=1)

df_list = df_revised.values.tolist()

faculty_dict ={}
value =[]

for i in range(len(df_list)):
    key = df_list[i][3]
    value = df_list[i][0:3]

    if key not in faculty_dict.keys():
        faculty_dict[key] = [value]
    else:
        faculty_dict[key].append(value)

n=0
for k,v in faculty_dict.items():
    if n < 3:
        print(k,v)
    else:
        break
    n += 1

professor_dict = {}

for i in range(len(df_list)):
    key = (df_list[i][3],df_list[i][4])
    value = df_list[i][0:3]
    if key not in professor_dict.keys():
        professor_dict[key]=[value]
    else:
        professor_dict[key].append(value)

n=0
for k,v in professor_dict.items():
    if n < 3:
        print(k,v)
    else:
        break
    n += 1

# to make sure it's printing the dict by sorted last name
sorted_key = sorted (professor_dict,key=lambda key : key[1])
for i in range (len(sorted_key)):
    key = sorted_key[i]
    value = professor_dict[sorted_key[i]]
    print (key,value)
