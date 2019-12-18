import pandas as pd
import numpy as np
import re
pd.set_option('display.max_columns', 100) # Show all columns when looking at dataframe
pd.set_option('display.max_rows', 500) # Show all columns when looking at dataframe

doc = []

with open('dates.txt') as file:
    for line in file:
        # print(line)
        doc.append(line)

# df = pd.Series(doc)
# print(df)


df = pd.Series(['ddd 04/20/09ddd',
                'ddd 4/20/09ddd',
                'ddd 4/3/09ddd',
                'ddd 04/20/2009ddd',
                'ddd 6/2008ddd',
                'ddd 12/2009ddd',
                'ddd 2009ddd',
                'ddd 2010ddd',
                'ddd 20 Mar 2009ddd',
                'ddd 20 March 2009ddd',
                'ddd 20 Mar. 2009ddd',
                'ddd 20 March, 2009ddd',
                'ddd Mar-20-2009ddd',
                'ddd Mar 20, 2009ddd',
                'ddd March 20, 2009ddd',
                'ddd Mar. 20, 2009ddd',
                'ddd Mar 20 2009ddd',
                'ddd April 1986ddd',
                'ddd Mar 20th, 2009ddd',
                'ddd Mar 21st, 2009ddd',
                'ddd Mar 22nd, 2009ddd',
                'Apr'])


def date_sorter():

    # Your code here
    '''
    04/20/2009; 04/20/09; 4/20/09; 4/3/09
    Mar-20-2009; Mar 20, 2009; March 20, 2009; Mar. 20, 2009; Mar 20 2009;
    (?P<month>\d?\d)[/|-](?P<day>([0-2]?[0-9])|([3][01]))[/|-](?P<year>[\d{4}|\d{2}])

    Mar 20th, 2009; Mar 21st, 2009; Mar 22nd, 2009
    (?P<month>[a-zA-Z]{3,})\.?-? ?(?P<day>\d\d?)(th|nd|st)?,?-? ?(?P<year>\d{4})

    20 Mar 2009; 20 March 2009; 20 Mar. 2009; 20 March, 2009
    (?P<day>\d?\d) ?(?P<month>[a-zA-Z]{3,})\.?,? (?P<year>\d{4})

    Feb 2009; Sep 2009; Oct 2010
    (?P<month>[A-Z][a-z]{3,}),?\.? (?P<year>\d{4})

    6/2008; 12/2009
    (?P<month>\d\d?)/(?P<year>\d{4})

    2009; 2010
    (?P<year>\d{4})
    '''

    # print(list(df.index))
    # df_filtered = df.str.extractall(r'(?P<month>\d?\d)[/-](?P<day>\d?\d)[/-](?P<year>\d{4})')
    # print(df_filtered)
    # # print([index[0] for index in df_filtered.index])
    # not_duplicated = ~df.index.isin([index[0] for index in df_filtered.index])    # ~ inverse from True to False and from False to True. Also df.index.isin find a unique index
    # # print(not_duplicated)
    # # print(df[not_duplicated])
    # x = df[not_duplicated].str.extractall(r'(?P<month>\d?\d)[/|-](?P<day>([0-2]?[0-9])|([3][01]))[/|-](?P<year>\d{2})')
    # print(x)
    # df_filtered = df_filtered.append(df[not_duplicated].str.extractall(r'(?P<month>\d?\d)[/-](?P<day>([0-2]?[0-9])|([3][01]))[/-](?P<year>\d{2})'))
    # print(df_filtered)
    # not_duplicated = ~df.index.isin([index[0] for index in df_ans.index])
    # df_ans = df_ans.append \
    #     (df[not_duplicated].str.extractall(r'(?P<day>\d?\d) ?(?P<month>[a-zA-Z]{3,})\.?,? (?P<year>\d{4})'))
    # not_duplicated = ~df.index.isin([index[0] for index in df_ans.index])
    # df_ans = df_ans.append(df[not_duplicated].str.extractall
    #     (r'(?P<month>[a-zA-Z]{3,})\.?-? ?(?P<day>\d\d?)(th|nd|st)?,?-? ?(?P<year>\d{4})'))
    # not_duplicated = ~df.index.isin([index[0] for index in df_ans.index])
    #
    # without_day = df[not_duplicated].str.extractall('(?P<month>[A-Z][a-z]{2,}),?\.? (?P<year>\d{4})')
    # without_day = without_day.append(df[not_duplicated].str.extractall(r'(?P<month>\d\d?)/(?P<year>\d{4})'))
    # without_day['day'] = 1
    # df_ans = df_ans.append(without_day)
    # not_duplicated = ~df.index.isin([index[0] for index in df_ans.index])
    #
    # without_month = df[not_duplicated].str.extractall(r'(?P<year>\d{4})')
    # without_month['day'] = 1
    # without_month['month'] = 1
    # df_ans = df_ans.append(without_month)
    # not_duplicated = ~df.index.isin([index[0] for index in df_ans.index])
    #
    # # Year
    # df_ans['year'] = df_ans['year'].apply(lambda x: '19' + x if len(x) == 2 else x)
    # df_ans['year'] = df_ans['year'].apply(lambda x: str(x))
    #
    # # Month
    # df_ans['month'] = df_ans['month'].apply(lambda x: x[1:] if type(x) is str and x.startswith('0') else x)
    # month_dict = {'February': 2, 'Dec': 12, 'Apr': 4, 'Jan': 1, 'Janaury': 1 ,'August': 8, 'October': 10
    #               ,'September': 9, 'Mar': 3, 'November': 11, 'Jul': 7, 'January': 1 ,'Feb': 2, 'May': 5, 'Aug': 8, 'Jun': 6, 'Sep': 9, 'Oct': 10, 'June': 6, 'March': 3, 'July': 7, 'Since': 1, 'Nov': 11, 'April': 4, 'Decemeber': 12, 'Age': 8}
    #
    # df_ans = df_ans.replace(month_dict)
    # df_ans['month'] = df_ans['month'].apply(lambda x: str(x))
    # df_ans['day'] = df_ans['day'].apply(lambda x: str(x))
    #
    # df_ans['date'] = df_ans['month'] + '/' + df_ans['day'] + '/' + df_ans['year']
    # df_ans['date'] = pd.to_datetime(df_ans['date'])
    #
    # df_ans = df_ans.sort_values(by='date')
    # return_rank = pd.Series(list(df_ans.index.labels[0]))
    #
    # return return_rank # Your answer here

    dateslist = []
    filter1 = r'(\d{1,2})[/-](\d{1,2})[/-](\d{2,4})'
    filter2 = r'((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec))[a-z]*[.]?[- ](\d{1,2})[,]?[- ](\d{4})'
    filter3 = r'(\d{1,2}) ((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec))[a-z]*[.,]? (\d{4})'
    filter4 = r'((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec))[a-z]* (\d{1,2})[a-z]{2}[,] (\d{4})'
    filter5 = r'((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec))[a-z]*[,]? (\d{4})'
    # for type 5 there for example line 339 Apr, 1998
    filter6 = r'(\d{1,2})[/](\d{4})'
    filter7 = r'\d{4}'
    month_dict = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06',
                  'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}

    for line in df:

        if len(re.findall(filter1, line)) != 0:
            date = list(re.findall(filter1, line)[0])  # change to list, because re.findall(filter1,s)[0] is a tuple, and we can't change value as tuple is immutable
            # print(date)

            if len(date[0]) == 1:
                date[0] = '0' + date[0]
            if len(date[1]) == 1:
                date[1] = '0' + date[1]
            if len(date[2]) == 2:  # change ab into 19ab
                if int(date[2]) > 0 & int(date[2]) < 19:
                    date[2] = '20' + date[2]
                else:
                    date[2] = '19' + date[2]
            dateslist.append(date[2] + date[0] + date[1])
            # print(dateslist)


        elif len(re.findall(filter2, line)) != 0:
            date = list(re.findall(filter2, line)[0])
            # print(date)
            date[0] = month_dict[date[0]]
            if len(date[1]) == 1:
                date[1] = '0' + date[1]
            dateslist.append(date[2] + date[0] + date[1])


        elif len(re.findall(filter3, line)) != 0:
            date = list(re.findall(filter3, line)[0])
            # print(date)
            if len(date[0]) == 1:
                date[0] = '0' + date[0]
            date[1] = month_dict[date[1]]
            dateslist.append(date[2] + date[1] + date[0])


        elif len(re.findall(filter4, line)) != 0:
            date = list(re.findall(filter4, line)[0])
            if len(date[1]) == 1:
                date[1] = '0' + date[1]
            date[0] = month_dict[date[0]]
            dateslist.append(date[2] + date[0] + date[1])


        elif len(re.findall(filter5, line)) != 0:
            # print(count) use this output to check for exceptions and mistakes
            date = list(re.findall(filter5, line)[0])
            # print(date)
            date[0] = month_dict[date[0]]
            dateslist.append(date[1] + date[0] + '01')


        elif len(re.findall(filter6, line)) != 0:
            date = list(re.findall(filter6, line)[0])
            # print(date)
            if len(date[0]) == 1:
                date[0] = '0' + date[0]
            dateslist.append(date[1] + date[0] + '01')


        elif len(re.findall(filter7, line)) != 0:
            date = re.findall(filter7, line)[0]
            # print(date)
            dateslist.append(date + '01' + '01')


        # else:
        #     print(line)  # because the question only mention part of the date form
            # try this you will find that there are 3 line with date 4-13-82 1-14-81 4-13-89, so


    dates = pd.Series(dateslist)
    # print(dates)
    dates.sort_values(inplace=True)
    # print(dates)
    assending_order = pd.Series(dates.index)

    return assending_order

print(date_sorter())