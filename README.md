![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Final Project: [AirBnB Dynamics in Berlin]

**[João Dias]**

**[Ironhack Data Analytics - August 2020]**

### Overview:

* I will try to identify the hotspots neighbourhoods in Berlin where Airbnb as a bigger impact and could affect housing price/gentrification"
	
* I will cluster the listing base on some features that could influence the area?
	* bigger impact- should mean more listings nearby, more rotativity, less availability, more profissionalise host, less personal.

* I will use unsupervised Machine learning Kmeans	


### Dataset

* [Inside Airbnb](http://insideairbnb.com/get-the-data.html) 


### Data Ingestion

* I created a jupyter notebook to download the data over time. (get_datasets.ipynb)
f you downloaded a dataset (either public or private), describe where you downloaded it and include the command to load the dataset.
* If you obtain the data via API/web scraping, provide the scripts.

### Data Wrangling and Cleaning

* Merging and cleaning with (merging.ipynb)


### Data Storage

* Dump your data to a MySQL database and/or a `.csv` file.

## Data Analysis

### Overview

Overview the general steps you will go through to analyze your data in order to test your hypothesis.

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

* Try to find the best features to cluster the hotspots, sing K-means.
* More data cleaning.
* Try different models and select one that is the simplest yet produce the best result.


## Conclusion

* The hot spots where Airbnb should have more impact on the neighbourhood is provide by the ploting files
* through the analysis of the descriptive information of the cluster it could identify 3 main groups of neighbourhoods
* The following neighborhoods
* The model was craft with just small amount of features but in the NLP we could had more features about the description of the house, and which kind of offers are shapping the market. 