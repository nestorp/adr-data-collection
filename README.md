# adr-data-collection
Author: Nestor Prieto Chavana

This is a set of Jupyter notebooks and python scripts used to perform data collection and cleaning for my MSc research project:
> Extraction of Adverse Drug Reaction Reports from Social Media: A Deep Learning Approach

Little work has gone into cleaning these up before publishing, so apologies if they're a bit messy. Most of the cell outputs have been removed to avoid publishing private information. 

#### Files & Directories

File Name | Description 
--- | --- 
`Reddit Data Collection PushShift API.ipynb` | Collect data from Reddit using the PushShift API
`twitsearch.py/` | Collect tweets using the Twitter search API via the Twython library
`twitstream.py/` | Collect tweets usingthe Twitter streaming API via the Twython library
`MHF Data Collection.ipynb` | Web scraping with the BeautifulSoup library
`Reddit Data Cleanup.ipynb` | Cleaning up Reddit dataset
`Twitter Data Cleanup.ipynb` | Cleaning up Twitter dataset
`MHF Data Cleanup.ipynb` | Cleaning up MHF dataset
`Making Graphs.ipynb` | Making graphs from result log files
