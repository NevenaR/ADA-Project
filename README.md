# ADA Project
## Abstract
Geolocated social media data gives a new perspective and insight on the life of a city or even a country. This data can indicate how a city developped/changed over years. With proper analysis, certain trends of the city can be identified and used to draw conclusions about the city in the near future. This project will be centered on Switzerland and we will study different regions in Switzerland. The goal is to create a temporal profile of the social and cultural trends of those cities over the years using georeferenced social media data, Flickr data in this case. 
## Data Description
As mentioned above, the analysis will be performed on Flickr data. There are two options how to get this data: it can be obtained online (Flickr image relationships https://snap.stanford.edu/data/web-flickr.html) or by using Flickr API. We will keep only geolocated data that comes from Switzerland. The analysis will be done using the metadata of Flickr images and in this projects we will focus specifically on tags. The idea is to filter those tags in order to obtain meaningful ones for a certain city that would describe the popularity of different things in that city. This would help us to build/identify a trend. The same can be done for different cities separately and analyse how it adds up on the scale of the whole country. We have yet to determine if we want to do analysis and comparison per canton or only for selected cities in Switzerland.
## Risks/Feasibility
The main challenge will be a Machine Learning task, which is to cluster the image metadata into different trends. We want to identify which tags are popular over the years, but we want to keep only those that are meaningful and add information to our analysis. This would help us to analyse the changes in the city over time and study its trend. Even though this is feasible, but the final result depends on how well we can perform the previous step. The analysis of the trend and possible predictions will depend on the findings again of the previous step. 
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