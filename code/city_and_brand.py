import pandas as pd
import os
import re
df = pd.read_csv(os.path.join('Data', 'Major_Cities_Moto_Data.csv'))

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

clean_product['Brand']=clean_product['Product'].apply(lambda x:x.split()[1] if x.split()[0].isnumeric() 
	else (x.split()[2] if x.split()[0].lower() == "used" else x))


including_brand=clean_product[['Product','Price','year','City','Brand']]

including_brand['Brand']= including_brand['Brand'].str.replace(r'[^\w\s]+', '')

including_brand['Brand']= including_brand['Brand'].str.lower()



including_brand = including_brand.drop_duplicates(subset = ['Product', 'Price'])
including_brand = including_brand.reset_index()[['Product',  'Price', 'year',  'City', 'Brand']]

including_brand = including_brand.drop_duplicates(subset = ['Product'])
including_brand = including_brand.reset_index()[['Product',  'Price', 'year',  'City', 'Brand']]

including_brand = including_brand.sort_values(by=['Product'])
including_brand = including_brand.reset_index()[['Product',  'Price', 'year',  'City', 'Brand']]


outpath = os.path.join('Data', "city_and_brand.csv")
including_brand.to_csv(outpath)
