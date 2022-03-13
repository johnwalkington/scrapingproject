import pandas as pd
df=pd.read_csv("/Users/minjinkang/Desktop/scrapingproject/code/Major_Cities_Moto_Data.csv")
import os
import re
df=df[df['Price']!=0]
df['year']=df['Product'].apply(lambda x: x.split()[-1] if x.split()[-1].isnumeric() and 
	int(x.split()[-1])>= 2000 else x)

df['year']=df['year'].apply(lambda x: x.split()[0] if x.split()[0].isnumeric() else x)

df['year']=df['year'].apply(lambda x: x.split()[1] if x.split()[0].lower() == "used" else x)
df['year']=df['year'].apply(lambda x: x if x.isnumeric() and len(x) ==4 else 'Unknown')

final=df[df['year'] != 'Unknown']
final=final.reset_index()[['Product','Price','year','City']]


final['word_count']=final.Product.str.count(' ')+1

having_one_word=final[final['word_count']==1].index
clean_product=final.drop(having_one_word)

clean_product['Brand']=clean_product['Product'].apply(lambda x:x.split()[1] if x.split()[0].isnumeric() else x)

including_brand=clean_product[['Product','Price','year','City','Brand']]

#print(including_brand)
# print(clean_product)


# len_list=[]
# for pro in final['Product']:
# 	len_list.append(len(pro.split()))


os.chdir("/Users/minjinkang/Desktop/scrapingproject/code")
including_brand.to_csv("product_price_year_city.csv")


