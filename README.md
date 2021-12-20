# US Rent Price Prediction 

The goal of the project is to analyze the rental postings across the United States and provide actionable insights to the users in form of graphs and intuitive user interface.

## Installation

This project requires Python 3.7+. Install the packages from requirements.txt

```sh
pip install -r requirements.txt
```

## Folder and File Structure

 - database folder contains the sqlite database with normalized tables
 - load_data.ipynb contains code to read the csv file, normalize the data to remove redundancy and insert it into a sqlite database. 
 - eda.ipynb contains code for the analysis of rental listings and deriving insights
 - model.ipynb contains code that applies Machine Learning algorithms to the data to predict the rental price of the house 
 - app.py contains code that runs the streamlit web server where the users provide their input to get estimated rental price. 
