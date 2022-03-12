import pandas as pd
from bs4 import BeautifulSoup
import requests
#import os 

my_headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OSX 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36", 
          "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"}
def url_to_df(url): 
    page = requests.get(url, headers = my_headers).content
    soup = BeautifulSoup(page, 'html.parser')
    mat = []
    
    for s in soup.find_all('a'): 
        if s.has_attr('href'):
            link = s['href']
            if link[-5:] == '.html': 
                lists = s.get_text(separator = '|').split('|')
                mat.append(lists)
    money = list()
    for listing in mat[::2]: 
        if len(listing) > 1: 
            money.append(listing[1])
        else: 
            money.append('$0')
    
    names = list()
    for name in mat[1::2]: 
        names.append(name[0])
    
    df = pd.DataFrame([names, money]).transpose()
    df.columns = ['Product',  'Price']
    df['Price'] = df['Price'].apply(lambda x: int(x[1:].replace(',', '')))
    return df
                

# Just feed it a url and you will get a dataframe output for that page. 

dfs = []
texas_cities = ['abilene', 'amarillo', 'beaumont', 'austin', 'collegestation', 
                'dallas', 'corpuschristi', 'mcallen', 'houston', 'sanantonio', 
               'easttexas', 'waco', 'galveston', 'brownsville']
for city in texas_cities: 
    base = 'https://' + city + '.craigslist.org/search/mca'
    df = url_to_df(base)
    df['City'] = city
    dfs.append(df)
    for i in range(120, 120*100, 120): 
        if url_to_df(base + '?s=' + str(i)).empty: 
            break
        df2 = url_to_df(base + '?s=' + str(i))
        df2['City'] = city
        dfs.append(df2)
        
final_df = pd.concat(dfs, ignore_index = True)

#os.chdir('/Users/patrickpoleshuk/Desktop/Python_Project/scrapingproject/code')
#final_df.to_csv('Major_Cities_Moto_Data.csv')
