#!/usr/bin/env python
# coding: utf-8

# In[41]:


#importing necessary libraries
import numpy as np
import pandas as pd
import os
from plotnine import *


# In[45]:


#read in data 
IN_PATH = os.path.join("Data", "new_final_clean.csv")
OUTPUT_DIR_PLOTS = "plots"
OUTPUT_DIR_DATA = "Data"


Motorcycles_CV =    pd.read_csv(IN_PATH)


# In[43]:


#data cleaning
    
Motorcycles_CV['City'] = Motorcycles_CV['City'].str.capitalize()

Motorcycles_CV['Brand'] = Motorcycles_CV['Brand'].str.capitalize()

Motorcycles_CV['Brand'] = Motorcycles_CV['Brand'].replace(['Hd','Harleydavidson','Harley'],'Harley Davidson')

Motorcycles_CV['Brand'] = Motorcycles_CV['Brand'].replace(['Ktm'],'KTM')

Motorcycles_CV['Brand'] = Motorcycles_CV['Brand'].replace(['Bmw'],'BMW')

Motorcycles_CV['City'] = Motorcycles_CV['City'].replace(['Corpuschristi'],'Corpus Christi')

Motorcycles_CV['City'] = Motorcycles_CV['City'].replace(['Collegestation'],'College Station')

Motorcycles_CV['City'] = Motorcycles_CV['City'].replace(['Easttexas'],'East Texas')

Motorcycles_CV['City'] = Motorcycles_CV['City'].replace(['Sanantonio'],'San Antonio')

Motorcycles_CV.loc[1567, 'Brand'] = 'Honda'


# In[44]:


#peeking at some of the data

Brand_counts = Motorcycles_CV['Brand'].value_counts()


# In[47]:


#exporting the CSV
write_df1 = Motorcycles_CV.to_csv(os.path.join(OUTPUT_DIR_DATA, "final_clean.csv"))


# In[48]:


#getting brand by city counts
brand_city = Motorcycles_CV.groupby(['Brand','City'])['Brand'].count().reset_index(name="Count")


#exporting csv
write_df2 = brand_city.to_csv(os.path.join(OUTPUT_DIR_DATA, "brand_city_counts.csv"))


# In[49]:


#creating brand popularity plot
plot_1 = (ggplot(Motorcycles_CV)
 + aes(x='Brand', fill= 'Brand')
 + geom_bar(size=20)
 + theme(axis_text_x = element_text(angle=45, hjust=1))
 + labs(title="Motorcycle Brand Popularity", 
         x="Brand", y = "Number of Listings")
)

#saving brand popularity plot to plot folder
ggsave(filename="plot1.png",
       plot=plot_1,
       device='png',
       dpi=300,
       height= 10,
       width= 10,
       path= os.path.join(OUTPUT_DIR_PLOTS)
      )

 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




