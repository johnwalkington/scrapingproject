import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import numpy as np
import pandas as pd
import os
import time

from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

f = os.path.join('code', 'product_price_year_city_final.csv')
df = pd.read_csv(f).iloc[:, 1:]
df = df.drop_duplicates(subset = ['Product', 'Price'])
df = df.reset_index()[['Product',  'Price', 'year',  'City']]

df = df.drop_duplicates(subset = ['Product'])
df = df.reset_index()[['Product', 'Price', 'year', 'City']]
# Using the old dataframe to merge into the coming json object. 

np.warnings.filterwarnings('ignore')

# Passing in a fake user-agent so the automated searches look more natural.

options = Options()
options.add_argument("window-size=1400,600")
from fake_useragent import UserAgent
ua = UserAgent()
user_agent = ua.random
options.add_argument(f'user-agent={user_agent}')

path = '/Users/patrickpoleshuk/Downloads/chromedriver 3'
driver = webdriver.Chrome(path, chrome_options=options)


json = {}
d = {}

# Going to append all characteristics of the motorcycles to a nested dictionary.

# THIS WILL TAKE HOURS TO RUN!!!

# I recommend that you turn off sleep mode on your computer and let it run
# overnight with the current time.sleep() settings.

for string, city in list(zip(df['Product'], df['City'])):
    d = {}
    try:
        if string not in json.keys():
            site = 'https://' + city + '.craigslist.org/'
            driver.get(site)
            search = driver.find_element_by_xpath('//*[@id="query"]')
            time.sleep(np.random.randint(2, 5))
            # Need to add a random sleep time so that the bot isn't detected,
            # and appears more like natural browsing.
            # (Can change the settings, but a quicker sleep time may result
            # in a blocked request).

            search.send_keys(string)
            search.send_keys(Keys.RETURN)
            driver.find_element_by_tag_name('h3').click()
            soup = BeautifulSoup(driver.page_source)
            out = []
            time.sleep(np.random.randint(2, 5))
            for s in soup.find_all('p', {'class':'attrgroup'}): 
                out.append(s.get_text(separator = '|').split('|'))
            out = out[1:][0]
            out = [o.replace('\n', '') for o in out if len(o) > 1]
            time.sleep(np.random.randint(2, 5))

            for i in range(len(out)-1): 
                if out[i].strip()[-1] == ':':
                    if out[i+1].strip()[-1] != ':':
                        d[out[i]] = out[i+1]
                    else: 
                        d[out[i]] = 'Unknown'

            if len(d.keys()) == len(d.values()): 
                json[string] = d

    except: 
        continue


# Parsing json object into a dataframe / merging with old dataframe above:


for d in json.keys(): 
    json[d] = { k.replace(':', ''): v for k, v in json[d].items() }
    json[d] = { k.strip(): v for k, v in json[d].items() }


sample = pd.DataFrame.from_dict(json.values(), orient='columns')
sample.reset_index(inplace = True)
sample['index'] = json.keys()


sample.columns = ['Product', 'fuel', 'odometer', 'paint_color', 'title_status',  'transmission', 
                 'condition', 'engine_displaement', 'type', 'VIN', 'make', 
                 'model']
new = pd.concat([sample,df[['Product', 'City']]], ignore_index=True).drop_duplicates('Product').reset_index()
del new['City']
del new['index']

final = new.merge(df, on = 'Product', how = 'inner')

out_path = os.path.join("code", 'Data_without_duplicates_and_all_info.csv')
final.to_csv(out_path)




