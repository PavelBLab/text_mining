import nltk
# from nltk.book import *


text = '''
Dictionaries might be a bit confusing to a new programmer. Try to think of it like a language dictionary. If you don’t know (or remember) exactly how “bijection” differs from “surjection” you can look the two terms up in the Oxford English Dictionary. The same principle applies when you print(d['hello']); except, rather than print a literary definition it prints the value associated with the keyword ‘hello’, as defined by you when you created the dictionary named d. In this case, that value is “0”.

Note that you use curly braces to define a dictionary, but square brackets to access things within it. The keys operation returns a list of keys that are defined in the dictionary.
'''

text_list = nltk.word_tokenize(text)
print(text_list)

# dict_comprehension = {k: text_list.count(k) for k in text_list}
# print(dict_comprehension)


# text_list = list(text1)
longest_word = ''
for word in text_list:
    if len(word) > len(longest_word):
        longest_word = word

print(longest_word)
print(len(longest_word))


word1 = '.......'

word2 ='sdscdscsdcs'

print(word1.isalpha())
print(word2.isalpha())




