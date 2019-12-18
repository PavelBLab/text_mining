from sklearn.feature_extraction.text import CountVectorizer

'''
https://machinelearningmastery.com/prepare-text-data-machine-learning-scikit-learn/
'''

# list of text documents
text = ["The quick brown fox jumped over the lazy dog the age The the the the the the the.",
        "age quick brown fox jumped over age lazy lazy dog age age age age age age age age age.",
        'fox',
        "The fox"
        'new']
print('list of text documents', text)

# create the transform
vectorizer = CountVectorizer()
print(type(vectorizer))
# tokenize and build vocab
vectorizer.fit(text)
print('tokenize and build vocab', vectorizer)

# summarize
print('summarize', vectorizer.vocabulary_)

# encode document
vector = vectorizer.transform(text)
# summarize encoded vector
print('summarize encoded vector')
print(vector)
print(vector.shape)
print(type(vector))
print(vector.toarray())


print('='.center(200, '='))
from sklearn.feature_extraction.text import TfidfVectorizer
# list of text documents
# text = ["The quick brown fox jumped over the lazy dog the the the.", "The dog dog dog.", "The fox", 'dog', 'the', 'the']
print(text)
# create the transform
vectorizer = TfidfVectorizer()
# tokenize and build vocab
vectorizer.fit(text)
# summarize
print('summarize')
print(type(vectorizer.vocabulary_))
print(vectorizer.vocabulary_)
print(vectorizer.idf_)
# encode document
vector = vectorizer.transform([text[0]])
# summarize encoded vector
print('summarize encoded vector')
print(vector)
print(type(vector))
print(vector.shape)
print(vector.toarray())
