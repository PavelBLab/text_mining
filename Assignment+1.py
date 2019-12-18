
# coding: utf-8

# ---
# 
# _You are currently looking at **version 1.1** of this notebook. To download notebooks and datafiles, as well as get help on Jupyter notebooks in the Coursera platform, visit the [Jupyter Notebook FAQ](https://www.coursera.org/learn/python-text-mining/resources/d9pwm) course resource._
# 
# ---

# # Assignment 1
# 
# In this assignment, you'll be working with messy medical data and using regex to extract relevant infromation from the data. 
# 
# Each line of the `dates.txt` file corresponds to a medical note. Each note has a date that needs to be extracted, but each date is encoded in one of many formats.
# 
# The goal of this assignment is to correctly identify all of the different date variants encoded in this dataset and to properly normalize and sort the dates. 
# 
# Here is a list of some of the variants you might encounter in this dataset:
# * 04/20/2009; 04/20/09; 4/20/09; 4/3/09
# * Mar-20-2009; Mar 20, 2009; March 20, 2009;  Mar. 20, 2009; Mar 20 2009;
# * 20 Mar 2009; 20 March 2009; 20 Mar. 2009; 20 March, 2009
# * Mar 20th, 2009; Mar 21st, 2009; Mar 22nd, 2009
# * Feb 2009; Sep 2009; Oct 2010
# * 6/2008; 12/2009
# * 2009; 2010
# 
# Once you have extracted these date patterns from the text, the next step is to sort them in ascending chronological order accoring to the following rules:
# * Assume all dates in xx/xx/xx format are mm/dd/yy
# * Assume all dates where year is encoded in only two digits are years from the 1900's (e.g. 1/5/89 is January 5th, 1989)
# * If the day is missing (e.g. 9/2009), assume it is the first day of the month (e.g. September 1, 2009).
# * If the month is missing (e.g. 2010), assume it is the first of January of that year (e.g. January 1, 2010).
# * Watch out for potential typos as this is a raw, real-life derived dataset.
# 
# With these rules in mind, find the correct date in each note and return a pandas Series in chronological order of the original Series' indices.
# 
# For example if the original series was this:
# 
#     0    1999
#     1    2010
#     2    1978
#     3    2015
#     4    1985
# 
# Your function should return this:
# 
#     0    2
#     1    4
#     2    0
#     3    1
#     4    3
# 
# Your score will be calculated using [Kendall's tau](https://en.wikipedia.org/wiki/Kendall_rank_correlation_coefficient), a correlation measure for ordinal data.
# 
# *This function should return a Series of length 500 and dtype int.*

# In[2]:


import pandas as pd

doc = []
with open('dates.txt') as file:
    for line in file:
        doc.append(line)

df = pd.Series(doc)
df.head(10)


# In[13]:


def date_sorter():
    df_filtered = df.str.extractall(r'(?P<month>\d?\d)[/|-](?P<day>\d?\d)[/|-](?P<year>\d{4})')
    # print(df_filtered)
    unused_index = ~df.index.isin([index[0] for index in df_filtered.index])    # ~ inverse from True to False and from False to True. Also df.index.isin find a unique index
    df_filtered = df_filtered.append(df[unused_index].str.extractall(r'(?P<month>\d?\d)[/|-](?P<day>([0-2]?[0-9])|([3][01]))[/|-](?P<year>\d{2})'))
    # print(df_filtered)
    unused_index = ~df.index.isin([index[0] for index in df_filtered.index])
    df_filtered = df_filtered.append(df[unused_index].str.extractall(r'(?P<day>\d?\d) ?(?P<month>[a-zA-Z]{3,})\.?,? (?P<year>\d{4})'))
    # print(df_filtered)
    unused_index = ~df.index.isin([index[0] for index in df_filtered.index])
    df_filtered = df_filtered.append(df[unused_index].str.extractall(r'(?P<month>[a-zA-Z]{3,})\.?-? ?(?P<day>\d\d?)(th|nd|st)?,?-? ?(?P<year>\d{4})'))
    # print(df_filtered)
    unused_index = ~df.index.isin([index[0] for index in df_filtered.index])

    without_day = df[unused_index].str.extractall('(?P<month>[A-Z][a-z]{2,}),?\.? (?P<year>\d{4})')
    without_day = without_day.append(df[unused_index].str.extractall(r'(?P<month>\d\d?)/(?P<year>\d{4})'))
    # print(without_day)
    without_day['day'] = 1
    df_filtered = df_filtered.append(without_day)
    # print(list(df_filtered.index))
    # print(df_filtered)
    unused_index = ~df.index.isin([index[0] for index in df_filtered.index])

    without_month = df[unused_index].str.extractall(r'(?P<year>\d{4})')
    without_month['day'] = 1
    without_month['month'] = 1
    # print(without_month )
    df_filtered = df_filtered.append(without_month)
    unused_index = ~df.index.isin([index[0] for index in df_filtered.index])

    # Year
    # print(int(df_filtered['year'][1]) + 1)
    df_filtered['year'] = df_filtered['year'].apply(lambda x: '19' + x if len(x) == 2 and int(x) > 19 else x)
    df_filtered['year'] = df_filtered['year'].apply(lambda x: '20' + x if len(x) == 2 and int(x) <= 19 else x)
    df_filtered['year'] = df_filtered['year'].apply(lambda x: str(x))
    # print(df_filtered)

    # # Month
    df_filtered['month'] = df_filtered['month'].apply(lambda x: x[1:] if type(x) is str and x.startswith('0') else x)
    # print(df_filtered['month'])
    month_dict = {'February': 2, 'Dec': 12, 'Apr': 4, 'Jan': 1, 'Janaury': 1, 'August': 8, 'October': 10,
                  'September': 9, 'Mar': 3, 'November': 11, 'Jul': 7, 'January': 1, 'Feb': 2, 'May': 5, 'Aug': 8,
                  'Jun': 6, 'Sep': 9, 'Oct': 10, 'June': 6, 'March': 3, 'July': 7, 'Since': 1, 'Nov': 11, 'April': 4,
                  'Decemeber': 12, 'Age': 8}

    df_filtered = df_filtered.replace(month_dict)
    # print(df_filtered)
    df_filtered['month'] = df_filtered['month'].apply(lambda x: str(x))
    df_filtered['day'] = df_filtered['day'].apply(lambda x: str(x))

    df_filtered['date'] = df_filtered['month'] + '/' + df_filtered['day'] + '/' + df_filtered['year']
    # print(df_filtered)
    df_filtered['date'] = pd.to_datetime(df_filtered['date'])
    # print(df_filtered['date'])

    df_filtered = df_filtered.sort_values(by='date')
    # print(df_filtered)
    assending_order = pd.Series(list(df_filtered.index.labels[0]))

    return assending_order
date_sorter()


# In[ ]:




