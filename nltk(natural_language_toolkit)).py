import nltk
# nltk.download()
from nltk.book import *
# text1 = 'Children shouldn\'t drink a sugary drink before bed.'


# text1
# sents()
# print(sent1)

text7
print(sent7)
print(len(sent7))
print('number of words', len(text7))
print('number of unique words', len(set(text7)))
print(list(set(text7))[:10])


# Frequency words
dist = FreqDist(text7)
# print(dist)
print('number of words', len(dist))

vocab1 = dist.keys()
print(list(vocab1)[:10])
print(dist[u'bomb'])
print([w for w in vocab1 if len(w) > 5 and dist[w] > 100])


# Normalization -> lower() or upper()
input1 = "List listed lists listing listings"
words1 = input1.lower().split(' ')
print('Normalization', words1)

# Stemming
stemmer = nltk.PorterStemmer()
print('Stemming', [stemmer.stem(x) for x in words1])

# Lemmatization
udhr = nltk.corpus.udhr.words('English-Latin1')
print(udhr[:20])
print([stemmer.stem(t) for t in udhr[:20]]) # Still Lemmatization)

WNlemma = nltk.WordNetLemmatizer()
print([WNlemma.lemmatize(t) for t in udhr[:20]])

# Tokenization of a word
text11 = "Children shouldn't drink a sugary drink before bed."
print(text11.split(' '))
print(nltk.word_tokenize(text11))

# Tokenization of a sentance

text12 = "This is the first sentence. A gallon of milk in the U.S. costs $2.99. Is this the third sentence? Yes, it is!"
sentences = nltk.sent_tokenize(text12)
print(len(sentences))
print(sentences)


# Advanced NLP Tasks with NLTK
# POS (part of speech) tagging
print(nltk.help.upenn_tagset('MD'))
text13 = nltk.word_tokenize(text11)
print(nltk.pos_tag(text13))

text14 = nltk.word_tokenize("Visiting aunts can be a nuisance")
print(nltk.pos_tag(text14))


# Parsing sentence structure
text15 = nltk.word_tokenize("Alice loves Bob")
# NP -> noun phrase and VP -> verb phrase
grammar = nltk.CFG.fromstring("""
S -> NP VP 
VP -> V NP
NP -> 'Alice' | 'Bob'
V -> 'loves'
""")

parser = nltk.ChartParser(grammar)
trees = parser.parse_all(text15)
for tree in trees:
    print(tree)



text16 = nltk.word_tokenize("I saw the man with a telescope")
# grammar1 = nltk.data.load('mygrammar.cfg')
# print(grammar1)

