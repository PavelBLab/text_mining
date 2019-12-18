import pandas as pd
import warnings
warnings.filterwarnings('ignore')
pd.set_option('display.max_rows', 500) # Show all columns when looking at dataframe



doc = []

with open('dates.txt') as file:
    for line in file:
        doc.append(line)
# print(doc)

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
                'ddd Mar-21-2009ddd',
                'ddd Mar 21, 2009ddd',
                'ddd March 21, 2009ddd',
                'ddd Mar. 21, 2009ddd',
                'ddd Mar 21 2009ddd',
                'ddd April 1986ddd',
                'ddd Mar 20th, 2009ddd',
                'ddd Mar 21st, 2009ddd',
                'ddd Mar 22nd, 2009ddd',
                'Apr'])

def date_sorter(data):

    data_filtered = data.str.extractall(r'(?P<month>\d{1,2})[/-](?P<day>\d{1,2})[/-](?P<year>(19|20)\d{2})')
    # print(data_filtered)
    unused_index = ~data.index.isin([index[0] for index in data_filtered.index])
    # print(unused_index)
    data_filtered = data_filtered.append(data[unused_index].str.extractall(r'(?P<month>\d{1,2})[/-](?P<day>\d{1,2})[/-](?P<year>\d{2})'))
    # print(data_filtered)
    unused_index = ~data.index.isin([index[0] for index in data_filtered.index])
    # print(unused_index)
    data_filtered = data_filtered.append(data[unused_index].str.extractall(r'(?P<month>\d{1,2})[/-](?P<year>(19|20)\d{2})'))
    # print(data_filtered)
    unused_index = ~data.index.isin([index[0] for index in data_filtered.index])
    data_filtered = data_filtered.append(data[unused_index].str.extractall(r'(?P<day>\d{1,2})[\s]*(?P<month>(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*)[.,\s-](?P<year>\d{4})'))
    # print(data_filtered)
    unused_index = ~data.index.isin([index[0] for index in data_filtered.index])
    data_filtered = data_filtered.append(data[unused_index].str.extractall(r'(?P<month>(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*)[.,\s-](?P<day>\d{1,2})?[,\s-]*(?P<year>\d{4})'))
    # print(data_filtered)
    unused_index = ~data.index.isin([index[0] for index in data_filtered.index])
    data_filtered = data_filtered.append(data[unused_index].str.extractall(r'(?P<month>(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*)[.,\s-](?P<day>\d{1,2})(?:st|nd|rd|th)[,\s]*(?P<year>\d{4})'))
    # print(data_filtered)
    unused_index = ~data.index.isin([index[0] for index in data_filtered.index])
    data_filtered = data_filtered.append(data[unused_index].str.extractall(r'(?P<year>(?:19|20)\d{2})'))
    # print(data_filtered)
    # print(len(data_filtered))
    del data_filtered[1]
    del data_filtered[2]
    del data_filtered[3]
    # print(data_filtered)

    data_filtered['day'] = data_filtered['day'].fillna('1')
    data_filtered['day'] = data_filtered['day'].apply(lambda x: x[1:] if type(x) is str and x.startswith('0') else x)
    data_filtered['month'] = data_filtered['month'].fillna('1')
    data_filtered['month'] = data_filtered['month'].apply(lambda x: x[1:] if type(x) is str and x.startswith('0') else x)
    data_filtered['year'] = data_filtered['year'].apply(lambda x: '19' + x if len(x) == 2 and int(x) > 19 else x)
    data_filtered['year'] = data_filtered['year'].apply(lambda x: '20' + x if len(x) == 2 and int(x) <= 19 else x)
    data_filtered['year'] = data_filtered['year'].apply(lambda x: str(x))

    month_dict = {'February': 2, 'Dec': 12, 'Apr': 4, 'Jan': 1, 'Janaury': 1, 'August': 8, 'October': 10,
                  'September': 9, 'Mar': 3, 'November': 11, 'Jul': 7, 'January': 1, 'Feb': 2, 'May': 5, 'Aug': 8,
                  'Jun': 6, 'Sep': 9, 'Oct': 10, 'June': 6, 'March': 3, 'July': 7, 'Since': 1, 'Nov': 11, 'April': 4,
                  'Decemeber': 12, 'Age': 8, '21': '1'}

    data_filtered = data_filtered.replace(month_dict)

    data_filtered['month'] = data_filtered['month'].apply(lambda x: str(x))
    data_filtered['day'] = data_filtered['day'].apply(lambda x: str(x))
    data_filtered['year'] = data_filtered['year'].apply(lambda x: str(x))


    data_filtered['date'] = data_filtered['month'] + '/' + data_filtered['day'] + '/' + data_filtered['year']
    data_filtered['date'] = pd.to_datetime(data_filtered['date'])
    data_filtered = data_filtered.sort_values(by='date')
    # print(data_filtered)
    order = pd.Series(list(data_filtered.index.labels[0]))

    return order



print(date_sorter(df))

