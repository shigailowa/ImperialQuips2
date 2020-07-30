import nltk
from nltk.tag import NgramTagger
from nltk.tag import PerceptronTagger
from nltk.corpus import conll2000
from nltk.corpus import webtext
from nltk.corpus import brown
from nltk.corpus import nps_chat


#general N-gram tagger
#works for every N
def ngram_tagger(n,train_data,backoff=None):
	Ngram_Tagger = NgramTagger(n,train_data,backoff=backoff)
	return(Ngram_Tagger)

#Backoff Tagging
def backoff_tagger(n,train_data):

	t0 = nltk.DefaultTagger('NN')

	taggers = [t0]

	for i in range(n):
		taggers.append(ngram_tagger(i+1,backoff=taggers[i],train_data = train_data))

	return taggers



##Greedy Average Perceptron tagger
#used and recommended by nltk
def perceptron_tagger(train_data):

	tagger = PerceptronTagger(load = False)
	tagger.train(train_data)

	return tagger


#Use best performing tagger as final tagger
def tag_words(phrase):
	
	text = nltk.word_tokenize(phrase)
	tags = nltk.pos_tag(text)
	return(tags)


if __name__ == '__main__':

	#different Datasets
	"""
	#Conll2000
	train_data = conll2000.tagged_sents('train.txt')
	test_data = conll2000.tagged_sents('test.txt')
	"""

	"""
	#Brown 
	size = int(len(brown.tagged_sents())*0.8)
	train_data = brown.tagged_sents()[:size]
	test_data = brown.tagged_sents()[size:]
	"""

	
	#NPS Chat
	size = int(len(nps_chat.tagged_posts())*0.8)
	train_data = nps_chat.tagged_posts()[:size]
	test_data = nps_chat.tagged_posts()[size:]


	#train different Taggers
	#simple Ngram
	unigram = ngram_tagger(1,train_data = train_data)
	bigram = ngram_tagger(2,train_data = train_data)
	trigram = ngram_tagger(3,train_data = train_data)
	fourgram = ngram_tagger(4,train_data = train_data)
	fivegram = ngram_tagger(5,train_data = train_data)

	#Backoff Taggers
	backoff1 = backoff_tagger(1,train_data)
	backoff2 = backoff_tagger(2,train_data)
	backoff3 = backoff_tagger(3,train_data)
	backoff4 = backoff_tagger(4,train_data)
	backoff5 = backoff_tagger(5,train_data)

	#Perceptron Tagger
	#perceptron = perceptron_tagger(train_data)

	#Evaluate Taggers
	print(unigram.evaluate(test_data))
	print(bigram.evaluate(test_data))
	print(trigram.evaluate(test_data))
	print(fourgram.evaluate(test_data))
	print(fivegram.evaluate(test_data))
	print(backoff1[-1].evaluate(test_data))
	print(backoff2[-1].evaluate(test_data))
	print(backoff3[-1].evaluate(test_data))
	print(backoff4[-1].evaluate(test_data))
	print(backoff5[-1].evaluate(test_data))
	#print(perceptron.evaluate(test_data))





