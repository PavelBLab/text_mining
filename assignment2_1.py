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
# print(list(text1))


def answer_eight():
    from collections import Counter
    import operator

    part_of_speech = nltk.pos_tag(text1)
    print(part_of_speech)
    #
    dictionary = {}
    for pos in part_of_speech:
    #     # print(pos)
        if pos[1] not in dictionary.keys():
            dictionary[pos[1]] = 1
        else:
            dictionary[pos[1]] += 1
    # print(dictionary)

    pos_list = sorted([(k, v) for k, v in dictionary.items()], key=operator.itemgetter(1), reverse=True)
    print(pos_list[:5])

    # print(nltk.pos_tag(text1))
    # print([tag for token, tag in nltk.pos_tag(text1)])
    # print(Counter([tag for token, tag in nltk.pos_tag(text1)]))
    # print(sorted(Counter([tag for token, tag in nltk.pos_tag(text1)]).items(), key=operator.itemgetter(1), reverse=True)[:5])  # Your answer here

    return pos_list


print(answer_eight())


from nltk.corpus import words
# nltk.download('words')

correct_spellings_list = words.words()


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

    # return result  # Your answer here

    # Example
    words_starts_with_c = [word for word in correct_spellings_list if word[0] == 'c']
    # print(words_starts_with_c)

    # print(list(set(nltk.ngrams(entries[0], n=3))))    # this breaks words by 3 letters
    # print([(nltk.jaccard_distance(set(nltk.ngrams(entries[0], n=3)), set(nltk.ngrams(word, n=3))), word) for word in words_starts_with_c])

print(answer_nine())