import pandas as pd
from bs4 import BeautifulSoup
import requests

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
                

# Here is an example:
example_url = 'https://austin.craigslist.org/search/mca?s=480'
# Just feed it a url and you will get a dataframe output for that page. 
print(url_to_df(example_url))
