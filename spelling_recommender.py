import nltk
from nltk.corpus import words
# nltk.download('words')

correct_spellings_list = words.words()
# print(correct_spellings_list)
# print(len(correct_spellings_list))



'''
For this part of the assignment you will create three different spelling recommenders, 
that each take a list of misspelled words and recommends a correctly spelled word for every word in the list.
For every misspelled word, the recommender should find find the word in correct_spellings that 
has the shortest distance*, and starts with the same letter as the misspelled word, and return that 
word as a recommendation.
*Each of the three different recommenders will use a different distance measure (outlined below).
Each of the recommenders should provide recommendations for the three default words provided: 
['cormulent', 'incendenece', 'validrate'].
'''

'''
Question 9
For this recommender, your function should provide recommendations for the three default words 
provided above using the following distance metric:
Jaccard distance on the trigrams of the two words.
This function should return a list of length three: 
['cormulent_reccomendation', 'incendenece_reccomendation', 'validrate_reccomendation'].
'''

# Example
import operator
entry = 'cormulent'
words_starts_with_c = [word for word in correct_spellings_list if word[0] == 'c'  and len(correct_spellings_list) > 2]
# print(words_starts_with_c)
print(list(nltk.ngrams(entry, n=4)))
print(list(set(nltk.ngrams(entry, n=4))))    # this breaks words by 3     letters
# distance_list_c = [(word, nltk.jaccard_distance(set(nltk.ngrams(entry, n=3)), set(nltk.ngrams(word, n=3)))) for word in words_starts_with_c]
# print(distance_list_c)
# print(sorted(distance_list_c, key=operator.itemgetter(1))[0])


def answer_nine(entries=['cormulent', 'incendenece', 'validrate']):
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

print(answer_nine())



'''
For this recommender, your function should provide recommendations for the three default 
words provided above using the following distance metric:
Jaccard distance on the 4-grams of the two words.
This function should return a list of length three: 
['cormulent_reccomendation', 'incendenece_reccomendation', 'validrate_reccomendation'].
'''

def answer_ten(entries=['cormulent', 'incendenece', 'validrate']):

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

# print(answer_ten())


def answer_eleven(entries=['cormulent', 'incendenece', 'validrate']):
    check_list = []
    result = []
    import operator
    distance_list = []
    for entry in entries:
        spell_list_words_starts_with_c_i_v = [correct_spelling for correct_spelling in correct_spellings_list if correct_spelling.startswith(entry[0]) and len(correct_spelling) > 2]
        distance_list = [(correct_spelling, nltk.edit_distance(entry, correct_spelling, transpositions=True)) for correct_spelling in spell_list_words_starts_with_c_i_v]
        check_list.append(sorted(distance_list, key=operator.itemgetter(1))[0])
        result.append(sorted(distance_list, key=operator.itemgetter(1))[0][0])
    # print(distance_list)
    # print(check_list)
    return result  # Your answer here


# print(answer_eleven())



