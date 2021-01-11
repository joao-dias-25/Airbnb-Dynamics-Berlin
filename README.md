![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Final Project: [AirBnB Dynamics in Berlin]

**[João Dias]**

**[Ironhack Data Analytics - August 2020]**

## Website analytics

* [website update 11-01-2021](https://share.streamlit.io/joao-dias-25/airbnb-dynamics-berlin/Berlinair.py)

## Overview:

* I will try to identify the hotspots neighbourhoods in Berlin where Airbnb as a bigger impact and could affect housing price/gentrification"
	
* I will cluster the listing base on some features that could influence the area?
	* bigger impact- should mean more listings nearby, more rotativity, less availability, more profissionalise host, less personal.

* I will use unsupervised Machine learning K-means	


### Dataset

* [Inside Airbnb](http://insideairbnb.com/get-the-data.html) 


### Data Ingestion

* I created a jupyter notebook to download the data over time. (get_datasets.ipynb)


### Data Wrangling and Cleaning

* Merging and cleaning with (merging.ipynb)


### Data Storage

* All the merge files will not be storage in github because of the size limitations


## Data Analysis

##Overview

* Analising the Airbnb Listings in Berlin over time

<img src="Listings in Berlin.png" width="800"/>

* features and possible hypoteses.

### Data Exploration and Visualization

* Understanding the evolution over time on the AirBnB listings
* How laws had an impact on the AirBnB listings
* Find the Hotspot listings.
* understanding the type of Host and their evolution.
* Identify the big players maybe vacation rental management companies (VRMs) 
* identify clusters of available apartments/house available
* Creating new quantifying features
* Create a model to identify which neibourhood is more prone to gentrification and monokultur
* Identify hotspots neighbourhoods.

### Model Training and Evaluation

* Try to find the best features to cluster the hotspots, using K-means.
* More data cleaning.
* Try different models and select one that is the simplest yet produce the best result.


## Conclusion

* The hot spots where Airbnb should have more impact on the neighbourhood is provide by the ploting files
* through the analysis of the descriptive information of the cluster it could identify 3 main groups of neighbourhoods
* The following neighborhoods
* The model was craft with just small amount of features but with NLP we could had more features about the description of the house, and which kind of offers are shapping the market. 