# -*- coding: utf-8 -*-
"""
Created on Wed May 29 18:12:11 2024

@author: mely7
"""

import pandas as pd

df = pd.read_csv("glassdoor_jobs.csv")

df = df[df['Salary Estimate'] != '-1']

#Make a hourly column in df where if the salary has 'per hour' is 1 then is 0
df['Hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
#Do the same thing for Employer provider
df['Employer_Provided_Salary'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary' in x.lower() else 0)

salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
#Remove the K and $ from the salary
minus_k = salary.apply(lambda x: x.replace('K', ' ').replace('$', ' '))
#Remove the 'per hour' from minus_k serie
minus_perhour = minus_k.apply(lambda x: x.lower().replace('per hour', ' ').replace('employer provided salary:', ' '))

df['Min_salary'] = minus_perhour.apply(lambda x: int(x.split('-')[0]))
df['Max_salary'] = minus_perhour.apply(lambda x: int(x.split('-')[1]))
df['AVG_salary'] = (df.Min_salary + df.Max_salary)/2

#get the company name
df['Company'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis = 1)

#get the state field
df['State'] = df['Location'].apply(lambda x: x.split(',')[1])
df.State.value_counts()

df['same_state'] = df.apply(lambda x: 1 if x['Location'] == x['Headquarters'] else 0, axis = 1)

#company_age
df['Age'] = df['Founded'].apply(lambda x: x if x < 1 else 2024 - x)

#parsing the job description
df['Python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['R_Studio'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() else 0)
df['Spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df['AWS'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df['Excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df['Excel'].value_counts()

#drop the first column
df.columns
df_out = df.drop('Unnamed: 0', axis = 1)

df_out.to_csv('data_salary_cleaned.csv', index = False)

pd.read_csv('data_salary_cleaned.csv')












