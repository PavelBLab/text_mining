
# coding: utf-8

# ---
# 
# _You are currently looking at **version 1.0** of this notebook. To download notebooks and datafiles, as well as get help on Jupyter notebooks in the Coursera platform, visit the [Jupyter Notebook FAQ](https://www.coursera.org/learn/python-text-mining/resources/d9pwm) course resource._
# 
# ---

# # Assignment 2 - Introduction to NLTK
# 
# In part 1 of this assignment you will use nltk to explore the Herman Melville novel Moby Dick. Then in part 2 you will create a spelling recommender function that uses nltk to find words similar to the misspelling. 

# ## Part 1 - Analyzing Moby Dick

# In[1]:


import nltk
# nltk.download('punkt')
import pandas as pd
import numpy as np

# If you would like to work with the raw text you can use 'moby_raw'
with open('moby.txt', 'r') as f:
    moby_raw = f.read()
    
# If you would like to work with the novel in nltk.Text format you can use 'text1'
moby_tokens = nltk.word_tokenize(moby_raw)
text1 = nltk.Text(moby_tokens)


# ### Example 1
# 
# How many tokens (words and punctuation symbols) are in text1?
# 
# *This function should return an integer.*

# In[2]:


def example_one():

    print(nltk.word_tokenize(moby_raw))
    return len(nltk.word_tokenize(moby_raw)) # or alternatively len(text1)

print(example_one())



# ### Example 2
# 
# How many unique tokens (unique words and punctuation) does text1 have?
# 
# *This function should return an integer.*

# In[3]:


def example_two():
    
    return len(set(nltk.word_tokenize(moby_raw))) # or alternatively len(set(text1))

example_two()


# ### Example 3
# 
# After lemmatizing the verbs, how many unique tokens does text1 have?
# 
# *This function should return an integer.*

# In[4]:


from nltk.stem import WordNetLemmatizer
# nltk.download('wordnet')

def example_three():

    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(w,'v') for w in text1]

    return len(set(lemmatized))

example_three()


# ### Question 1
# 
# What is the lexical diversity of the given text input? (i.e. ratio of unique tokens to the total number of tokens)
# 
# *This function should return a float.*

# In[5]:


def answer_one():
    
    total_tokens = len(nltk.word_tokenize(moby_raw))
#     print(total_tokens)
    unique_tokens = len(set(nltk.word_tokenize(moby_raw)))
#     print(unique_tokens)
    
    return unique_tokens/total_tokens

answer_one()


# ### Question 2
# 
# What percentage of tokens is 'whale'or 'Whale'?
# 
# *This function should return a float.*

# In[6]:


def answer_two():
    
    total_tokens = nltk.word_tokenize(moby_raw)
#     print(total_tokens[:10])
#     lemmatizer = WordNetLemmatizer()
#     lemmatized = [lemmatizer.lemmatize(w) for w in total_tokens]
#     print(lemmatized)
#     return len([x for x in lemmatized if x == 'whale' or x == 'Whale'])/len(total_tokens) *100

#     print(list(text1.vocab())[:10])
#     print(text1.vocab()['whale'])
    return (text1.vocab()['whale'] + text1.vocab()['Whale']) / len(nltk.word_tokenize(moby_raw)) * 100

answer_two()


# ### Question 3
# 
# What are the 20 most frequently occurring (unique) tokens in the text? What is their frequency?
# 
# *This function should return a list of 20 tuples where each tuple is of the form `(token, frequency)`. The list should be sorted in descending order of frequency.*

# In[7]:


def answer_three():
    import operator
    
    total_tokens = nltk.word_tokenize(moby_raw)
    unique_tokens = set(total_tokens)
    
#     print(type(text1))
#     print(moby_raw)
#     print(total_tokens)
    
    
    
#     test = ['w', 'w', 'k', 't', 't', 't', 't', 't', 'o', 'h']
    
    dictionary = {}
    for word in total_tokens:
#         print(word)
        if word not in dictionary.keys():
            dictionary[word] = 1
        else:
            dictionary[word] += 1
      
    frequency_token_list = sorted([(v, k) for k, v in dictionary.items()], reverse=True)[:20]
    token_frequency_list = [(k, v) for v, k in frequency_token_list]
    
#     print(sorted(text1.vocab().items(), key=operator.itemgetter(1), reverse=True)[:20])
    
    return token_frequency_list

#     return sorted(text1.vocab().items(), key=operator.itemgetter(1), reverse=True)[:20]

answer_three()


# ### Question 4
# 
# What tokens have a length of greater than 5 and frequency of more than 150?
# 
# *This function should return an alphabetically sorted list of the tokens that match the above constraints. To sort your list, use `sorted()`*

# In[8]:


def answer_four():
       
    total_tokens = nltk.word_tokenize(moby_raw)

    dictionary = {}
    for word in total_tokens:
#         print(word)
        if word not in dictionary.keys():
            dictionary[word] = 1
        else:
            dictionary[word] += 1
#     print(dictionary)
    
    search_list = [word for word in dictionary.keys() if len(word) > 5 and dictionary[word] > 150]
    
#     print(sorted(search_list, key=lambda s: s.lower())
    return sorted(search_list)

answer_four()


# ### Question 5
# 
# Find the longest word in text1 and that word's length.
# 
# *This function should return a tuple `(longest_word, length)`.*

# In[9]:


def answer_five():
    
    text_list = list(text1)
    
    longest_word = ''
    for word in text_list:
        if len(word) > len(longest_word):
            longest_word = word

#     print(longest_word)
#     print(len(longest_word))   
    
    
    return (longest_word, len(longest_word))

answer_five()


# ### Question 6
# 
# What unique words have a frequency of more than 2000? What is their frequency?
# 
# "Hint:  you may want to use `isalpha()` to check if the token is a word and not punctuation."
# 
# *This function should return a list of tuples of the form `(frequency, word)` sorted in descending order of frequency.*

# In[10]:


def answer_six():
    
    text_list = list(text1)
    
    dictionary = {}
    for word in text_list:
#         print(word)
        if word not in dictionary.keys():
            dictionary[word] = 1
        else:
            dictionary[word] += 1
          
    search_list = [(v, k) for k, v in dictionary.items() if k.isalpha() == True and dictionary[k] > 2000]
#     search_list = []
    
#     for k, v in dictionary.items():
#         if k.isalpha() == True and dictionary[k] > 2000:
#             search_list.append((v, k))
    
    
    
    return sorted(search_list, reverse=True)

answer_six()


# ### Question 7
# 
# What is the average number of tokens per sentence?
# 
# *This function should return a float.*

# In[11]:


def answer_seven():
    
    total_sentances = nltk.sent_tokenize(moby_raw)
#     print(len(total_sentances))
#     print(total_sentances)
    number_tokens = [len(nltk.word_tokenize(sentance)) for sentance in total_sentances]
#     print(len(number_tokens))
     
    return np.average(number_tokens)

answer_seven()


# ### Question 8
# 
# What are the 5 most frequent parts of speech in this text? What is their frequency?
# 
# *This function should return a list of tuples of the form `(part_of_speech, frequency)` sorted in descending order of frequency.*

# In[12]:


def answer_eight():
    nltk.download('averaged_perceptron_tagger')
    from collections import Counter
    import operator

#     part_of_speech = nltk.pos_tag(text1)
    # # print(part_of_speech)
    #
#     dictionary = {}
#     for pos in part_of_speech:
    #     # print(pos)
#         if pos[1] not in dictionary.keys():
#             dictionary[pos[1]] = 1
#         else:
#             dictionary[pos[1]] += 1
    # print(dictionary)

#     pos_list = sorted([(k, v) for k, v in dictionary.items()], key=operator.itemgetter(1), reverse=True)[:5]
#     print(pos_list[:5])

    # print(nltk.pos_tag(text1))
    # print([tag for token, tag in nltk.pos_tag(text1)])
    # print(Counter([tag for token, tag in nltk.pos_tag(text1)]))
    # print(sorted(Counter([tag for token, tag in nltk.pos_tag(text1)]).items(), key=operator.itemgetter(1), reverse=True)[:5])  # Your answer here

#     return pos_list
    return sorted(Counter([tag for token, tag in nltk.pos_tag(text1)]).items(), key=operator.itemgetter(1), reverse=True)[:5] # Your answer here

answer_eight()


# ## Part 2 - Spelling Recommender
# 
# For this part of the assignment you will create three different spelling recommenders, that each take a list of misspelled words and recommends a correctly spelled word for every word in the list.
# 
# For every misspelled word, the recommender should find find the word in `correct_spellings` that has the shortest distance*, and starts with the same letter as the misspelled word, and return that word as a recommendation.
# 
# *Each of the three different recommenders will use a different distance measure (outlined below).
# 
# Each of the recommenders should provide recommendations for the three default words provided: `['cormulent', 'incendenece', 'validrate']`.

# In[14]:


from nltk.corpus import words
nltk.download('words')

correct_spellings = words.words()


# ### Question 9
# 
# For this recommender, your function should provide recommendations for the three default words provided above using the following distance metric:
# 
# **[Jaccard distance](https://en.wikipedia.org/wiki/Jaccard_index) on the trigrams of the two words.**
# 
# *This function should return a list of length three:
# `['cormulent_reccomendation', 'incendenece_reccomendation', 'validrate_reccomendation']`.*

# In[16]:


def answer_nine(entries=['cormulent', 'incendenece', 'validrate']):
    correct_spellings_list = correct_spellings
    result = []
    distance_list = []
    import operator
    # print(correct_spellings_list)
    # print(len(correct_spellings_list))
    for entry in entries:
        spell_list_words_starts_with_c_i_v = [correct_spelling for correct_spelling in correct_spellings_list if correct_spelling.startswith(entry[0]) and len(correct_spelling) > 2]
        # print(spell_list)
        distance_list = [(correct_spelling, nltk.jaccard_distance(set(nltk.ngrams(entry, n=3)), set(nltk.ngrams(correct_spelling, n=3)))) for
                         correct_spelling in spell_list_words_starts_with_c_i_v]

        # result.append(sorted(distance_list, key=operator.itemgetter(1)))
        result.append(sorted(distance_list, key=operator.itemgetter(1))[0][0])

    # print(distance_list)
    # print(result)

    return result  # Your answer here
    
answer_nine()


# ### Question 10
# 
# For this recommender, your function should provide recommendations for the three default words provided above using the following distance metric:
# 
# **[Jaccard distance](https://en.wikipedia.org/wiki/Jaccard_index) on the 4-grams of the two words.**
# 
# *This function should return a list of length three:
# `['cormulent_reccomendation', 'incendenece_reccomendation', 'validrate_reccomendation']`.*

# In[17]:


def answer_ten(entries=['cormulent', 'incendenece', 'validrate']):
    correct_spellings_list = correct_spellings
    result = []
    import operator
    for entry in entries:
        spell_list_words_starts_with_c_i_v = [correct_spelling for correct_spelling in correct_spellings_list if
                                              correct_spelling.startswith(entry[0]) and len(correct_spelling) > 2]
        distance_list = [(correct_spelling,
                          nltk.jaccard_distance(set(nltk.ngrams(entry, n=4)), set(nltk.ngrams(correct_spelling, n=4))))
                         for
                         correct_spelling in spell_list_words_starts_with_c_i_v]

        # result.append(sorted(distance_list, key=operator.itemgetter(1)))
        result.append(sorted(distance_list, key=operator.itemgetter(1))[0][0])

    # print(distance_list)
    # print(result)
    return result  # Your answer here
    
answer_ten()


# ### Question 11
# 
# For this recommender, your function should provide recommendations for the three default words provided above using the following distance metric:
# 
# **[Edit distance on the two words with transpositions.](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance)**
# 
# *This function should return a list of length three:
# `['cormulent_reccomendation', 'incendenece_reccomendation', 'validrate_reccomendation']`.*

# In[18]:


def answer_eleven(entries=['cormulent', 'incendenece', 'validrate']):
    correct_spellings_list = correct_spellings 
    result = []
    import operator
    for entry in entries:
        spell_list = [spell for spell in correct_spellings if spell.startswith(entry[0]) and len(spell) > 2]
        distance_list = [(spell, nltk.edit_distance(entry, spell, transpositions=True)) for spell in spell_list]

        result.append(sorted(distance_list, key=operator.itemgetter(1))[0][0])
    
    return result# Your answer here 
    
answer_eleven()


# In[ ]:




