
# _You are currently looking at **version 1.1** of this notebook. To download notebooks and datafiles, as well as get help on Jupyter notebooks in the Coursera platform, visit the [Jupyter Notebook FAQ](https://www.coursera.org/learn/python-text-mining/resources/d9pwm) course resource._


# # Assignment 3
# 
# In this assignment you will explore text message data and create models to predict if a message is spam or not. 

import pandas as pd
import numpy as np

spam_data = pd.read_csv('spam.csv')

spam_data['target'] = np.where(spam_data['target']=='spam',1,0)
print(len(spam_data))
print(spam_data.head(10))


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(spam_data['text'], 
                                                    spam_data['target'], 
                                                    random_state=0)

# ### Question 1
# What percentage of the documents in `spam_data` are spam?
#
# *This function should return a float, the percent value (i.e. $ratio * 100$).*

def answer_one():

    return float(len(spam_data[spam_data['target'] == 1])/len(spam_data)) * 100

print(answer_one())


# ### Question 2
# 
# Fit the training data `X_train` using a Count Vectorizer with default parameters.
# 
# What is the longest token in the vocabulary?
# 
# *This function should return a string.*

from sklearn.feature_extraction.text import CountVectorizer

def answer_two():
    import operator
    vect = CountVectorizer().fit(X_train)
    # print(vect.get_feature_names()[:2000])

    token = ''
    for i in vect.get_feature_names():
        if len(i) > len(token):
            token = i
    # print(token)

    return sorted([(i, len(i)) for i in vect.get_feature_names()], key=operator.itemgetter(1), reverse=True)[0][0]

print(answer_two())


# ### Question 3
# 
# Fit and transform the training data `X_train` using a Count Vectorizer with default parameters.
# 
# Next, fit a fit a multinomial Naive Bayes classifier model with smoothing `alpha=0.1`. Find the area under the curve (AUC) score using the transformed test data.
# 
# *This function should return the AUC score as a float.*

from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import roc_auc_score

def answer_three():

    vect = CountVectorizer().fit(X_train)
    # print(vect)
    # print(len(vect.get_feature_names()))
    '# THIS IS VERY IMPORTANT'
    # print(vect.vocabulary_)     # this gives you word: frequency appeares in a text
    # print([(k, v) for k, v in vect.vocabulary_.items()][:5])
    X_train_transform = vect.transform(X_train)
    # print(X_train_vect_transf[0])

    clf = MultinomialNB(alpha=0.1).fit(X_train_transform, y_train)
    # print(clf)
    prediction = clf.predict(vect.transform(X_test))

    return float(roc_auc_score(y_test, prediction))

print(answer_three())


# ### Question 4
# 
# Fit and transform the training data `X_train` using a Tfidf Vectorizer with default parameters.
# 
# What 20 features have the smallest tf-idf and what 20 have the largest tf-idf?
# 
# Put these features in a two series where each series is sorted by tf-idf value and then alphabetically by feature name.
# The index of the series should be the feature name, and the data should be the tf-idf.
# 
# The series of 20 features with smallest tf-idfs should be sorted smallest tfidf first, the list of 20 features with largest tf-idfs should be sorted largest first. 
# 
# *This function should return a tuple of two series
# `(smallest tf-idfs series, largest tf-idfs series)`.*

from sklearn.feature_extraction.text import TfidfVectorizer

def answer_four():

    import operator

    vect = TfidfVectorizer().fit(X_train)
    # print(vect)
    # print(len(vect.get_feature_names()))
    # print(vect.vocabulary_)
    # print([(k, v) for k, v in vect.vocabulary_.items()][:5])
    X_train_vect_transf = vect.transform(X_train)
    # print(X_train_vect_transf)


    feature_names = np.array(vect.get_feature_names())
    idfs = vect.idf_
    # print('idfs', idfs)
    names_idfs = sorted(list(zip(feature_names, idfs)), key=operator.itemgetter(1))
    # print('names_idfs', names_idfs[:5])

    smallest = names_idfs[:20]
    smallest_tfidfs_series = pd.Series([features[1] for features in smallest], index=[features[0] for features in smallest])
    # print(smallest_tfidfs_series)

    largest = sorted(names_idfs, key=operator.itemgetter(1), reverse=True)[:20]
    largest_tfidfs_series = pd.Series([features[1] for features in largest], index=[features[0] for features in largest])
    # print(largest_tfidfs_series)

    return (smallest_tfidfs_series, largest_tfidfs_series)

print(answer_four())


# ### Question 5
# 
# Fit and transform the training data `X_train` using a Tfidf Vectorizer ignoring terms that have a document frequency strictly lower than **3**.
# 
# Then fit a multinomial Naive Bayes classifier model with smoothing `alpha=0.1` and
# compute the area under the curve (AUC) score using the transformed test data.
# 
# *This function should return the AUC score as a float.*

def answer_five():

    vect = TfidfVectorizer(min_df=3).fit(X_train)    # min_df  ignoring terms that have a document frequency strictly lower than 3
    X_train_transform = vect.transform(X_train)

    clf = MultinomialNB(alpha=0.1).fit(X_train_transform, y_train)

    X_test_transform = vect.transform(X_test)
    # prediction_prob = clf.predict_proba(X_test_transform)[:, 1]
    # print('prediction_prob', prediction_prob)
    prediction = clf.predict(X_test_transform)

    return float(roc_auc_score(y_test, prediction))

print(answer_five())


# ### Question 6
# 
# What is the average length of documents (number of characters) for not spam and spam documents?
# 
# *This function should return a tuple (average length not spam, average length spam).*

def answer_six():

    spam_data['text_length'] = spam_data['text'].str.len()
    # spam_data['text_length'] = spam_data['text'].apply(lambda x: len(x))
    # print(spam_data)

    spam_part = np.mean(spam_data.loc[spam_data['target'] == 1, 'text_length'])
    no_spam_part = np.mean(spam_data.loc[spam_data['target'] == 0, 'text_length'])

    return (no_spam_part, spam_part)

print(answer_six())


# <br>
# <br>
# The following function has been provided to help you combine new features into the training data:



def add_feature(X, feature_to_add):
    """
    Returns sparse feature matrix with added feature.
    feature_to_add can also be a list of features.
    """
    from scipy.sparse import csr_matrix, hstack
    return hstack([X, csr_matrix(feature_to_add).T], 'csr')


# ### Question 7
# 
# Fit and transform the training data X_train using a Tfidf Vectorizer ignoring terms that have a document frequency strictly lower than **5**.
# 
# Using this document-term matrix and an additional feature, **the length of document (number of characters)**, fit a Support Vector Classification model with regularization `C=10000`. Then compute the area under the curve (AUC) score using the transformed test data.
# 
# *This function should return the AUC score as a float.*


from sklearn.svm import SVC

def answer_seven():

    import warnings
    warnings.filterwarnings('ignore')

    vect = TfidfVectorizer(min_df=5).fit(X_train)
    X_train_transf = vect.transform(X_train)
    X_train_transf_length = add_feature(X_train_transf, X_train.str.len())

    clf = SVC(C=10000).fit(X_train_transf_length, y_train)

    X_test_transf = vect.transform(X_test)
    X_test_transf_length = add_feature(X_test_transf, X_test.str.len())

    prediction = clf.predict(X_test_transf_length)
    # print(prediction)

    return float(roc_auc_score(y_test, prediction))

print(answer_seven())


# ### Question 8
# 
# What is the average number of digits per document for not spam and spam documents?
# 
# *This function should return a tuple (average # digits not spam, average # digits spam).*

# x = 'wfweewfwe ewfewfwe 23424 wfewf 324324 55 7'
# print('===>', ''.join([a for a in x if a.isdigit()]))
def answer_eight():

    # spam_data['number_digits'] = spam_data['text'].apply(lambda x: len(''.join([a for a in x if a.isdigit()])))
    # print(spam_data['number_digits'][:5])
    spam_data['number_digits'] = spam_data['text'].str.findall(r'[0-9]').str.len()
    print(spam_data['number_digits'][:5])

    spam_avrg_digit = np.mean(spam_data.loc[spam_data['target'] == 1, 'number_digits'])
    # print(spam_avrg_digit)
    no_spam_avrg_digit = np.mean(spam_data.loc[spam_data['target'] == 0, 'number_digits'])
    
    return (no_spam_avrg_digit, spam_avrg_digit)

print(answer_eight())


# ### Question 9
# 
# Fit and transform the training data `X_train` using a Tfidf Vectorizer ignoring terms that have a document frequency strictly lower than **5** and using **word n-grams from n=1 to n=3** (unigrams, bigrams, and trigrams).
# 
# Using this document-term matrix and the following additional features:
# * the length of document (number of characters)
# * **number of digits per document**
# 
# fit a Logistic Regression model with regularization `C=100`. Then compute the area under the curve (AUC) score using the transformed test data.
# 
# *This function should return the AUC score as a float.*

from sklearn.linear_model import LogisticRegression

def answer_nine():
    
    vect = TfidfVectorizer(min_df=5, ngram_range=(1, 3)).fit(X_train)
    # print(vect.vocabulary_)
    X_train_transform = vect.transform(X_train)
    X_train_transform_length = add_feature(X_train_transform, [X_train.str.len(), X_train.str.findall(r'[0-9]').str.len()])

    clf = LogisticRegression(C=100).fit(X_train_transform_length, y_train)

    X_test_transform = vect.transform(X_test)
    X_test_transform_length = add_feature(X_test_transform, [X_test.str.len(), X_test.str.findall(r'[0-9]').str.len()])
    prediction = clf.predict(X_test_transform_length)

    return float(roc_auc_score(y_test, prediction))

print(answer_nine())


# ### Question 10
# 
# What is the average number of non-word characters (anything other than a letter, digit or underscore) per document for not spam and spam documents?
# 
# *Hint: Use `\w` and `\W` character classes*
# 
# *This function should return a tuple (average # non-word characters not spam, average # non-word characters spam).*

def answer_ten():

    spam_data['non-word characters'] = spam_data['text'].str.findall(r'\W').str.len()
    # print(spam_data.head())

    spam_part = np.mean(spam_data.loc[spam_data['target'] == 1, 'non-word characters'])
    no_spam_part = np.mean(spam_data.loc[spam_data['target'] == 0, 'non-word characters'])

    return (no_spam_part, spam_part)

print(answer_ten())


# ### Question 11
# 
# Fit and transform the training data X_train using a Count Vectorizer ignoring terms that have a document frequency strictly lower than **5** and using **character n-grams from n=2 to n=5.**
# 
# To tell Count Vectorizer to use character n-grams pass in `analyzer='char_wb'` which creates character n-grams only from text inside word boundaries. This should make the model more robust to spelling mistakes.
# 
# Using this document-term matrix and the following additional features:
# * the length of document (number of characters)
# * number of digits per document
# * **number of non-word characters (anything other than a letter, digit or underscore.)**
# 
# fit a Logistic Regression model with regularization C=100. Then compute the area under the curve (AUC) score using the transformed test data.
# 
# Also **find the 10 smallest and 10 largest coefficients from the model** and return them along with the AUC score in a tuple.
# 
# The list of 10 smallest coefficients should be sorted smallest first, the list of 10 largest coefficients should be sorted largest first.
# 
# The three features that were added to the document term matrix should have the following names should they appear in the list of coefficients:
# ['length_of_doc', 'digit_count', 'non_word_char_count']
# 
# *This function should return a tuple `(AUC score as a float, smallest coefs list, largest coefs list)`.*

def answer_eleven():

    pd.set_option('display.max_columns', 100)  # Show all columns when looking at dataframe
    pd.set_option('display.max_rows', 100)  # Show all columns when looking at dataframe
    # vect = CountVectorizer(min_df=5, ngram_range=(2, 5)).fit(X_train)
    # print(vect.get_feature_names()[:30])
    # print(len(vect.get_feature_names()))

    vect = CountVectorizer(min_df=5, ngram_range=(2, 5), analyzer='char_wb').fit(X_train)
    # print(vect.vocabulary_)

    for k, v in vect.vocabulary_.items():
        print(k, ':', v)

    # print(vect.get_feature_names()[:30])
    # print(len(vect.get_feature_names()))

    X_train_transform = vect.transform(X_train)
    X_train_transform_length = add_feature(X_train_transform, [X_train.str.len(),
                                                               X_train.str.findall(r'[0-9]').str.len(),
                                                               X_train.str.findall(r'\W').str.len()])

    # for i in X_train_transform[0].toarray()[0]:
    #     print(i)

    clf = LogisticRegression(C=100).fit(X_train_transform_length, y_train)

    X_test_transform = vect.transform(X_test)
    X_test_transform_length = add_feature(X_test_transform, [X_test.str.len(),
                                                             X_test.str.findall(r'[0-9]').str.len(),
                                                             X_test.str.findall(r'\W').str.len()])
    prediction = clf.predict(X_test_transform_length)

    feature_names = np.array(vect.get_feature_names())



    feature_names = np.array(vect.get_feature_names() + ['length_of_doc', 'digit_count', 'non_word_char_count'])
    # print(len(np.array(vect.get_feature_names())))
    sorted_coef_index = clf.coef_[0].argsort()
    # print(len(sorted_coef_index))
    # print(clf.coef_[0])
    # print(sorted_coef_index)
    #
    smallest_coefs_list = list(feature_names[sorted_coef_index[:10]])
    # # print(len(largest_coefs_list))
    largest_coefs_list = list(feature_names[sorted_coef_index[:-11:-1]])

    return (roc_auc_score(y_test, prediction), smallest_coefs_list, largest_coefs_list)

print(answer_eleven())

