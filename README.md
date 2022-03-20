# scrapingproject

# Documentation
# source of dataset - Craigslist
# we scraped data from Craigslist using Beautiful Soup
# we wanted to find information on motorcycle prices correlated to motorcycle coasting for the Austin, TX area

Requirements for reporting analysis:
The goal of this project is to learn to scrape data from Craigslist and learn interesting information related to motorcycles.

Methodology:
Once we decided to use Craigslist to scrape data for motorcycle sales, we decided to use BeautifulSoup to parse html codes of various cities in Texas. This created a data frame of product names and prices. After this, we worked within the data frame to find information for the year it was made and the brand from the product listing name. We did this because the product name had a lot of information about the motorcycle already; most of them had the brand, year, and other pertinent information in the product listing itself. After this, we used Selenium with the product names to automate search queries; this would loop through the product column to find information like color and odometer. 

Description of project and findings:

-Limitations: When using Selenium, there was a cap on how much you can parse on the product title.
-Extensions:
-Plots:

Source of datasets:

Data collection methods:
