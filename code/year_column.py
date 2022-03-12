import pandas as pd
df=pd.read_csv("/Users/minjinkang/Desktop/scrapingproject/code/Major_Cities_Moto_Data.csv")

import re
df=df[df['Price']!=0]
df['year']=df['Product'].apply(lambda x: x.split()[-1] if x.split()[-1].isnumeric() and 
	int(x.split()[-1])>= 2000 else x)

df['year']=df['year'].apply(lambda x: x.split()[0] if x.split()[0].isnumeric() else x)

df['year']=df['year'].apply(lambda x: x.split()[1] if x.split()[0].lower() == "used" else x)
df['year']=df['year'].apply(lambda x: x if x.isnumeric() and len(x) ==4 else 'Unknown')

final=df[df['year'] != 'Unknown']
final=final.reset_index()[['Product','Price','year','City']]


print(final)