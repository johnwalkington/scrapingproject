import pandas as pd
import os
import re

df=pd.read_csv("/Users/minjinkang/Desktop/scrapingproject/Data_without_duplicates_and_all_info.csv")
df2 = pd.read_csv("/Users/minjinkang/Desktop/scrapingproject/code/city_and_brand.csv")


result=pd.merge(df,df2,on='Product',how='left')

result=result[['Product', 'fuel', 'odometer', 'paint_color', 'title_status',  'transmission', 'condition', 'engine_displaement', 
'type', 'VIN', 'Price_x', 'year_x','City_x','Brand']]

os.chdir("/Users/minjinkang/Desktop/scrapingproject/code")
result.to_csv("new_final_clean_2.csv")