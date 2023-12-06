import nltk
from nltk.corpus import stopwords

reviews = open('ice_cream_reviews.txt')
stopwords = set(stopwords.words("english"))

for review in reviews:
    print('n/')
#    print(review)
    tokens = nltk.word_tokenize(review)
#    print(tokens)
    pos_tag = nltk.pos_tag(tokens)
#    print(pos_tag)
    new_text = []
    for tag in pos_tag: #adjetives: JJ,JJR,JJS. Noun: NN, NNP, NNS.
#        if tag[1] == 'JJ' or tag[1] == 'JJR' or tag[1] == 'JJS':
#           print(tag)
        if tag[0] not in stopwords:
            new_text.append(tag[0])
    print('\noriginal')
    print(review)
    print('\nNew')
    print("".join(new_text))