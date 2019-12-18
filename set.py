string = 'to be or not to be be be be be'
string_split = string.split(' ')


# set() returns only unique words
print(set(string_split))

# print(list(reversed([1, 2, 3] + [4, 5])))
def append_list(new_list, word):

    # for x in len(new_list):
    new_list = new_list + [word]
    updated_list = []
    count = len(new_list) - 1

    for i in range(len(new_list)):
        updated_list = updated_list + [new_list[count]]
        # print(updated_list)
        # print(new_list[count])
        count -= 1

    return updated_list
print(append_list([1,2,3,4,5], 'new string'))


# from sklearn import naive_bayes, svm
# clf = naive_bayes.MultinomialNB().fit()
#
# from nltk.classify import NaiveBayesClassifier
# clf = NaiveBayesClassifier.train()
# clf.classify()
# clf.classify_many()
# # nltk.classify.util.accuracy


