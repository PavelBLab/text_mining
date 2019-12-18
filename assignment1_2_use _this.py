import pandas as pd
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

    return assending_order  # Your answer here

print(date_sorter())