import pandas as pd
pd.set_option('display.max_columns', 100) # Show all columns when looking at dataframe
pd.set_option('display.max_rows', 500) # Show all columns when looking at dataframe

doc = []

with open('dates.txt') as file:
    for line in file:
        # print(line)
        doc.append(line)

df = pd.Series(doc)
# print(df)


test = pd.Series(['ddd 04/20/09ddd',
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
# print(test)


def date_sorter(data):

    # ?P<column_name> -> this names a column
    filter1 = '\d{1,2}[/-]\d{1,2}[/-](?:19|20)\d{2}'    # 04/20/2009
    filter2 = '\d{1,2}[/-]\d{1,2}[/-]\d{2}'    # 04/20/09; 4/20/09; 4/3/09
    filter3 = '\d{1,2}[/-](?:19|20)\d{2}'      # 6/2008; 12/2009
    filter4 = '(?:19|20)\d{2}'                 # 2009; 2010

    # 20 Mar 2009; 20 March 2009; 20 Mar. 2009; 20 March, 2009
    filter5 = '\d{1,2}[\s]*(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z.,\s-]*\d{4}'
    # Mar-20-2009; Mar 20, 2009; March 20, 2009; Mar. 20, 2009; Mar 20 2009; April 1986
    filter6 = '(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z.,\s-]*(?:\d{1,2}[,\s-]*)?\d{4}'
    # Mar 20th, 2009; Mar 21st, 2009; Mar 22nd, 2009
    filter7 = '(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z.,\s-]*\d{1,2}(?:st|nd|rd|th)[,\s]*\d{4}'

    '''
    # 20 Mar 2009; 20 March 2009; 20 Mar. 2009; 20 March, 2009
    # Mar-20-2009; Mar 20, 2009; March 20, 2009; Mar. 20, 2009; Mar 20 2009;
    # Mar 20th, 2009; Mar 21st, 2009; Mar 22nd, 2009
    filter = '(?:\d{1,2}[,\s-]*)?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z.,\s-]*(?:\d{1,2}[,\s-]*)?\d{4}'
    '''

    data_filtered = data.str.findall(r'{}|{}|{}|{}|{}|{}|{}'.format(filter1, filter2, filter3, filter4, filter5, filter6, filter7))
    # print(data_filtered)

    # extraction1 = data.str.extractall(r'(\d{1,2})[/-](\d{1,2})[/-]((?:19|20)\d{2})[a-z.,\s]')
    # extraction1.reset_index(inplace=True)
    # extraction1_index = extraction1['level_0']
    # # print(extraction1)
    # extraction2 = data.str.extractall(r'(\d{1,2})[/-](\d{1,2})[/-](\d{2})[a-z.,\s]')
    # extraction2.reset_index(inplace=True)
    # extraction2_index = extraction2['level_0']
    # # print(extraction2)
    # # x = pd.concat([extraction1, extraction2])
    # # print(extraction1.append(extraction2))
    # # print(x)
    #
    # extraction3 = data.str.extractall('(\d{1,2})[/-]((?:19|20)\d{2})')
    # extraction3.reset_index(inplace=True)
    # extraction3_index = extraction3['level_0']
    # # print(extraction3)
    #
    # a6 = df.str.extractall(r'(\d{1,2})[/](\d{4})')
    # a6.reset_index(inplace=True)
    # a6_index = a6['level_0']
    # save = []
    # for i in a6_index:
    #     if not (i in a1_index.values):
    #         save.append(i)
    # save = np.asarray(save)
    # a6 = a6[a6['level_0'].isin(save)]
    #
    # # extraction4 = data.str.extractall()
    # # extraction5 = data.str.extractall()
    # # extraction6 = data.str.extractall()
    # # extraction7 = data.str.extractall()
    #
    #
    #

    return data_filtered

print(date_sorter(test))