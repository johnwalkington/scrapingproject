## Report

### Goal
The goal of this project is to learn how to scrape data from Craigslist and to discover interesting trends in Texans' tastes for motorcycles.

### Methodology - Data Scraping
Once we decided to use Craigslist to scrape data for motorcycle listings, we used BeautifulSoup to parse html codes of various cities in Texas. This created a data frame of product listings with their respective prices. The script also uses Pandas, os, and request. After this, we used this data frame to extract information for year and brand using the product listing. 

Once we had this data, we used Selenium and product listings to automate search queries; this loops through the product column to find information like color and odometer. We did this to automate the process and export the data to a dataframe rather than manually searching and clicking on each listing in Craigslist. The script also uses pandas and numpy packages.

### Description of project and findings

#### Methodology - Data Visualization

We then made plots to better visualize the scraped data. We wanted to find information about the most popular brands, average price by motorcycle brand, color popularity and favorite motorcycle brand by city. To do this, we used ggplot within plotnine. Additionally, we used matplotlib and seaborn to plot the color popularity data.

![](plots/plot1.png)

Plot 1 shows motorcycle brand popularity across all cities in Texas that were included in the dataset. We can see here that Harley Davidson is the most popular brand at over 600 listings. Honda, Kawasaki and Yamaha are the next most popular and all have around 200 listings. In terms of economic analysis, it seems that the tarrifs levied on motorcycle imports in 1983 have had a lasting effect on motorcycle tastes in the US. 

![](plots/plot2.png)

Plot 2 shows the average price by motorcycle brand across all cities in Texas that were included in the dataset. Polaris has the highest average price at over $20,000. Canam, Ducati, Harley Davidson, and Indian all have the next highest average price of around $15,000. Looking at the plot, there also appears to be a clear division between high end and low end motorcycles with Polaris, Canam, Ducati, Harley Davidson, and Indian incorporating the higher end. 

Polaris' price could be skewed high due to the following reasons:

- Polaris bought Indian motorcycles in 2011, but we don't think anyone is misnaming Indian as Polaris in the plots

- Polaris owns Victory

- Polaris doesn't make motorcycles under their own brand, just the car-like slingshots, which could be the reason why the average price is so high. Slingshots are federally classifed as three-wheeled motorcycles.



![](plots/plot3.png)

Plot 3 shows the color popularity across all cities in Texas that were included in the dataset and also had a color included in the listing. Black is the most popular color at around 350 listings. Red is the second most popular at around 125 listings. Custom color could refer to a variety of colors, but we assume it means a non-conventional paint job. 

![](plots/plot4.png)

Plot 4 shows favorite brand by city. We only include cities that had a diversity of listings avaiable, which were Austin, Dallas and Houston. Harley Davidson was the most popular brand in all three cities, which corroborates Plot 1. All three cities follow a similar pattern and distribution, with the exception of Dallas having a higher proportion of Yamaha listings than Austin and Houston do (Honda is the second most popular overall).

#### Limitations
When scraping from Craigslist, we only had the option of choosing from cities, and not states. With doing this, products from nearby cities were included in the scrape, but not included in the search query since these were city specific. This caused us to lose some data. Some other issues were that some data was left blank in the search queries and there were many advertisements (fake listings), which we cleaned. Both of these caused us to lose data for the analysis. When using Selenium, there was a cap on how much you can parse on the product title, so we only parsed with color and odometer. Another issue with Selenium scraper on a more broad level happens when the scraper opens chrome and types the product listing. When it is querying the listings, usually only one listing pops up, and on a rare instance, the scraper can click on a duplicate listing rather than a relevant listing. Lastly, when scraping data from Craigslist, the results were dependent on the day, so if we were to do this another day, we would get different results since listings are added, updated or deleted every day.

#### Extensions
Some extensions of this analysis would be scraping data over longer periods of time and expanding the scraping process in different locations and categories in Craigslist. We could scrape over different days, potentially different seasons to see how the information varies. Additionally, we could also scrape in various states across the US and see if the most popular brands, average price by motorcycle brand and color popularity vary by state. Lastly, we could use this same scraping process in different categories on Craigslist. Here we focused on motorcycle product listings, but we could expand this into different automotive listings, such as cars. On a more broad overview, we could expand into different product categories as well. Another broad extension would be incorporating better methods to prevent data loss.


### Reproducibility
In order to rerun the analysis, you will need to install the requirements which contains all the necessary packages, and then run the files in a certain order.

In order to install the requirements, you will need to run "pip3 install -r requirements.txt"

Once these pacakges are installed, the order of running the files is as follows:

These first three scripts are used to scrape the initial data from Craigslist, and then re-scrape for more specific data, like odometer, color, transmission, etc. These scripts are not neccessary to reproduce our analysis as the final dataset is included in the data folder. The Selenium scraper may run into fake user issues and Google Vertex AI issues, Craigslist has a chance to detect the scraper, and reject the scraper's request for data. Because the Google Vertex AI may or may not have a browser, the Selenium Scraper may not open Chrome properly.

1. url_to_dataframe.py
2. city_and_brand.py
3. selenium_scraper.py

These two scripts are meant to create the final data frames, clean the data, and create our plots. These are the two necessary scripts to recreate our analysis, using CSVs that are already in the in the data folder. 

4. making_final.py
5. plots_scraping_project.py
