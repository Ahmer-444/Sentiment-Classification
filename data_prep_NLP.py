import nltk
import gensim
from nltk.corpus import brown


sentences = brown.sents()
model = gensim.models.Word2Vec(sentences, min_count=1)

'''
paragraph = u"Hi, this is my first sentence. And this is my second."
sentences = nltk.sent_tokenize(paragraph)

sentence_list = []
for sentence in sentences:
    sentence_list.append(nltk.word_tokenize(sentence))

print (sentence_list)

# Append sentence
print (' '.join(sentence_list[0]))

'''
