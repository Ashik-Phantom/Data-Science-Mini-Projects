from bs4 import BeautifulSoup as bs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

soup = bs(open("skillrackdata.html"))  
table=soup.select("td.gridcell") 

name=[]
dept=[] 
ID=[]
gold=[] 
silver=[] 
bronze=[]

for i in range(50):
    if i%2==0:
        c=0
        for j in table[i].stripped_strings:
            if c==0:
                name.append(j)
                c+=1
                continue
            if c==1:
                dept.append(j)
                c+=1
                continue
            if c==2:
                ID.append(j)
                c=0
                continue
    else:
        c=0
        for j in table[i].stripped_strings:
            if c==0 and j.isdigit():
                gold.append(j)
                c+=1 
                continue
            if c==1 and j.isdigit():
                silver.append(j)
                c+=1 
                continue
            if c==2 and j.isdigit():
                bronze.append(j)
                c=0
                continue
result=[]
for i in range(len(name)):
    value=[]
    value.append(name[i])
    value.append(dept[i])
    value.append(ID[i])
    value.append(int(gold[i]))
    value.append(int(silver[i]))
    value.append(int(bronze[i]))
    result.append(value)

df=pd.DataFrame(result,columns=["Name","Dept","ID","Gold","Silver","Bronze"])
df.columns.name = 'Rank'
df.index = df.index + 1
print(df)

temp_result=[i[1:] for i in result]
temp_df=pd.DataFrame(temp_result,columns=["Dept","ID","Gold","Silver","Bronze"],index=name)
df.columns.name = 'Rank'

print(temp_df)

b=df['Bronze'].describe()
s=df['Silver'].describe() 
g=df['Gold'].describe()

print(b,s,g)
