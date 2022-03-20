
Requirements for reporting analysis:
The goal of this project is to learn to scrape data from Craigslist and learn interesting information related to motorcycles.

Methodology:
Once we decided to use Craigslist to scrape data for motorcycle sales, we decided to use BeautifulSoup to parse html codes of various cities in Texas. This created a data frame of product names and prices. After this, we worked within the data frame to find information for the year it was made and the brand from the product listing name. We did this because the product name had a lot of information about the motorcycle already; most of them had the brand, year, and other pertinent information in the product listing itself. After this, we used Selenium with the product names to automate search queries; this would loop through the product column to find information like color and odometer. We did this to automate the process and get it all on a dataframe instead of manually searching and clicking on each one in Craigslist.

Description of project and findings:

-Limitations: 
When scraping from Craigslist, we only had the option of choosing from cities, and not states. With doing this, products from nearby cities were included in the scrape, but not included in the search query since these were city specific. This caused us to lose some data. Additionally, some data was left blank in the search queries. While using Craiglists, there were many advertisements, which we cleaned. The blank data and cleaning the advertisements also caused us to lose data for the analysis.
When using Selenium, there was a cap on how much you can parse on the product title, so we only parsed with color and odometer.


-Extensions:
-Plots:
Polaris is skewed high, potentially due to the following reasons:
-Polaris bought Indian motorcycles in 2011, but we don't think anyone is misnaming Indian as Polaris in the plots
-Polaris owns Victory
-Polaris doesn't make motorcycles under their own brand, just the car-like slingshots, which could be the reason why the average price is so high

Source of datasets:

Data collection methods:
