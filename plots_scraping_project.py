#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 12:52:53 2022

@author: jaymegerring
"""

#importing necessary libraries
import numpy as np
import pandas as pd

#read in data 
Motorcycles_CV =\
    pd.read_csv('/Users/jaymegerring/Downloads/GitHub/scrapingproject/code/new_final_clean.csv') 
    
Motorcycles_CV['City'] = Motorcycles_CV['City'].str.capitalize()

Motorcycles_CV['Brand'] = Motorcycles_CV['Brand'].replace(['hd','harleydavidson','harley'],'Harley Davidson')

Motorcycles_CV['City'] = Motorcycles_CV['City'].replace(['Corpuschristi'],'Corpus Christi')

Motorcycles_CV['City'] = Motorcycles_CV['City'].replace(['Collegestation'],'College Station')

Motorcycles_CV['City'] = Motorcycles_CV['City'].replace(['Easttexas'],'East Texas')

Motorcycles_CV['City'] = Motorcycles_CV['City'].replace(['Sanantonio'],'San Antonio')

Brand_counts = Motorcycles_CV['Brand'].value_counts()













