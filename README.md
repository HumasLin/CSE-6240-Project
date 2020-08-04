# CSE-6240-Project

<b>100cities_details_indeed.py:</b> This program can scrape 100 data files from Indeed.com as job postings from these 100 cities, with information including salary, location, job title,
job description, company, etc.

<b>locs.txt:</b> This file is a pure text file of 100 big cities in US

<b>merge.py:</b> This program can merge all the job posting information from 100 cities in US to produce a integrated dataset. 

<b>salary_prediction.ipynb:</b> This notebook is able to execute following tasks:
-transform specific salary values into salary levels;
-predict job postings without salary values based on vectorized job description;
-categorize job postings into 16 industries by counting the number of keywords from each industry;
-calculate the confidence interval of gender scores in each industry/salary level.

*When executed, make sure all the data files are in the same directory.
