# ADA Project
## Abstract
Geolocated social media data gives a new perspective and insight on the life of a city or even a country. This data can indicate how a city developped/changed over years. With proper analysis, certain trends of the city can be identified and used to draw conclusions about the city in the near future. This project will be centered on Switzerland and we will study different regions in Switzerland. The goal is to find differences between data across Switzerland and also to create a temporal profile of the social and cultural trends of some locations over the years using georeferenced social media data, Flickr data in this case. 
## Data Description
As mentioned above, the analysis will be performed on Flickr data. Since we didn't have ready data available, we needed to scrape the data. The Flickr API was used for that purposes and more details about the script and scraping can be found in the scraping folder. 
Only data geolocated from Switzerland was used. The overall result of data scraping produced about 2.8 million images mostly from years 2005 till 2017. The resulting data was stored in parts on github and it can be found together with all the transformations done on it in the data folder. 
The analysis was concenrated on the metadata of Flickr images, specifically we used tags. 
There were multiple issues we encountaired during the work with tags, namely multiple languages and special characters, spelling mistakes and all this made the analysis of the tags more complicated. We have focused on two different axes: 
* One was to analyse tags per canton and observe the differences 
* Second was the analysis per time, where we found the most popular locations for each year based on number of images and number of users. 
The idea is to filter those tags in order to obtain meaningful ones for a certain city that would describe the popularity of different things in that city. 
## Deliverables
Visual representation should allow an easy comparison between different cities, social and cultural differences in a city over the years. This would be our main deliverable. The results of the analysis and data would be given and documented as well.
## Timeplan
* Checkpoint (Mid December)
    * Collect data
    * Study dataset
    * Determine whether we should focus on cantons or cities
    * Find popular tags per city/canton
* Mini-Symposium (End of January) 
    * Refine the popular tag selection
    * Analyse metadata and identify trends
    * Perform comparison and additional analysis for certain findings
    * Draw conclusions on large scale
    * Visulization of conclusions
