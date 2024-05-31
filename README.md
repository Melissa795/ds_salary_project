# Data Scientist Salary Analysis and Prediction

This project aims to analyze and predict the salaries of Data Scientists using a dataset obtained from Glassdoor through web scraping. The project includes data cleaning, exploratory data analysis (EDA), and the development of a regression model to predict salaries based on various factors.

## Project Overview

The goal of this project is to:
1. **Collect data**: Scrape salary data for Data Scientists from Glassdoor.
2. **Data Cleaning**: Process and clean the scraped data to ensure it is suitable for analysis.
3. **Exploratory Data Analysis (EDA)**: Perform EDA to understand the underlying patterns and insights within the data.
4. **Model Building**: Develop and train a regression model to predict Data Scientist salaries.
5. **Model Deployment**: Deploy the regression model for practical use.

## Dataset

The dataset was collected by scraping Glassdoor for salary information related to Data Scientist positions. The data includes various features such as job title, company name, location, and salary estimates.

## Steps and Methodology

### 1. Data Collection

Web scraping was performed on Glassdoor to collect the dataset. Python libraries such as `BeautifulSoup` and `requests` were used to scrape the necessary information.

### 2. Data Cleaning

Data cleaning involved the following steps:
- Removing duplicates and irrelevant data.
- Handling missing values by imputation or removal.
- Standardizing the format of the data (e.g., converting salary estimates to numerical values).
- Correcting inconsistencies in categorical data (e.g., standardizing job titles and company names).

### 3. Exploratory Data Analysis (EDA)

EDA was performed to uncover insights and patterns within the data. This included:
- Visualizing the distribution of salaries.
- Analyzing the impact of different factors (e.g., location, company size) on salaries.
- Identifying correlations between various features and salary.

### 4. Model Building

A regression model was developed to predict Data Scientist salaries. The process involved:
- Selecting relevant features for the model.
- Splitting the data into training and test sets.
- Training the model using algorithms such as Linear Regression, Decision Trees, or Random Forest.
- Evaluating the model's performance using metrics like R-squared and Mean Absolute Error (MAE).

### 5. Model Deployment

The final regression model was deployed for practical use. This involved:
- Saving the trained model using serialization techniques (e.g., `pickle` or `joblib`).
- Creating a user interface or API to allow users to input new data and obtain salary predictions.

## Requirements

To run the code in this repository, you will need:

- Python 3.11
- Required Python libraries (pandas, matplotlib, seaborn, nltk, wordcloud

## Acknowledgments

- Special thanks to Ken Jee for guiding me through the entire project.
