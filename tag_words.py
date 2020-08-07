import nltk
from nltk.tag import NgramTagger
from nltk.tag import PerceptronTagger
from nltk.corpus import conll2000
from nltk.corpus import webtext
from nltk.corpus import brown
from nltk.corpus import nps_chat
import matplotlib.pyplot as plt
import numpy as np

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

	#print(tag_words("play football and watch netflix"))

	#different Datasets
	
	#Conll2000
	train_data_1 = conll2000.tagged_sents('train.txt')
	test_data_1 = conll2000.tagged_sents('test.txt')

	
	#Brown 
	size = int(len(brown.tagged_sents())*0.8)
	train_data_2 = brown.tagged_sents()[:size]
	test_data_2 = brown.tagged_sents()[size:]

	
	#NPS Chat
	size = int(len(nps_chat.tagged_posts())*0.8)
	train_data = nps_chat.tagged_posts()[:size]
	train_data_3 = [x for i, x in enumerate(train_data) if i!=4257]
	test_data_3 = nps_chat.tagged_posts()[size:]


	"""	
	#train different Taggers
	#simple Ngram
	unigram_1 = ngram_tagger(1,train_data = train_data_1)
	bigram_1 = ngram_tagger(2,train_data = train_data_1)
	trigram_1 = ngram_tagger(3,train_data = train_data_1)
	fourgram_1 = ngram_tagger(4,train_data = train_data_1)
	fivegram_1 = ngram_tagger(5,train_data = train_data_1)

	unigram_2 = ngram_tagger(1,train_data = train_data_2)
	bigram_2 = ngram_tagger(2,train_data = train_data_2)
	trigram_2 = ngram_tagger(3,train_data = train_data_2)
	fourgram_2 = ngram_tagger(4,train_data = train_data_2)
	fivegram_2 = ngram_tagger(5,train_data = train_data_2)

	unigram_3 = ngram_tagger(1,train_data = train_data_3)
	bigram_3 = ngram_tagger(2,train_data = train_data_3)
	trigram_3 = ngram_tagger(3,train_data = train_data_3)
	fourgram_3 = ngram_tagger(4,train_data = train_data_3)
	fivegram_3 = ngram_tagger(5,train_data = train_data_3)
	"""

	backoff1_1 = backoff_tagger(1,train_data = train_data_1)
	backoff2_1 = backoff_tagger(2,train_data = train_data_1)
	backoff3_1 = backoff_tagger(3,train_data = train_data_1)
	backoff4_1 = backoff_tagger(4,train_data = train_data_1)
	backoff5_1 = backoff_tagger(5,train_data = train_data_1)

	backoff1_2 = backoff_tagger(1,train_data = train_data_2)
	backoff2_2 = backoff_tagger(2,train_data = train_data_2)
	backoff3_2 = backoff_tagger(3,train_data = train_data_2)
	backoff4_2 = backoff_tagger(4,train_data = train_data_2)
	backoff5_2 = backoff_tagger(5,train_data = train_data_2)

	backoff1_3 = backoff_tagger(1,train_data = train_data_3)
	backoff2_3 = backoff_tagger(2,train_data = train_data_3)
	backoff3_3 = backoff_tagger(3,train_data = train_data_3)
	backoff4_3 = backoff_tagger(4,train_data = train_data_3)
	backoff5_3 = backoff_tagger(5,train_data = train_data_3)

	"""
	#Backoff Taggers
	backoff1 = backoff_tagger(1,train_data_new)
	backoff2 = backoff_tagger(2,train_data_new)
	backoff3 = backoff_tagger(3,train_data_new)
	backoff4 = backoff_tagger(4,train_data_new)
	backoff5 = backoff_tagger(5,train_data_new)

	
	#Perceptron Tagger
	perceptron = perceptron_tagger(train_data_new)
	"""
	
	#Evaluate Taggers
	conll_acc = []
	conll_acc.append(backoff1_1[-1].evaluate(test_data_1))
	conll_acc.append(backoff2_1[-1].evaluate(test_data_1))
	conll_acc.append(backoff3_1[-1].evaluate(test_data_1))
	conll_acc.append(backoff4_1[-1].evaluate(test_data_1))
	conll_acc.append(backoff5_1[-1].evaluate(test_data_1))

	brown_acc = []
	brown_acc.append(backoff1_2[-1].evaluate(test_data_2))
	brown_acc.append(backoff2_2[-1].evaluate(test_data_2))
	brown_acc.append(backoff3_2[-1].evaluate(test_data_2))
	brown_acc.append(backoff4_2[-1].evaluate(test_data_2))
	brown_acc.append(backoff5_2[-1].evaluate(test_data_2))

	nps_acc = []
	nps_acc.append(backoff1_3[-1].evaluate(test_data_3))
	nps_acc.append(backoff2_3[-1].evaluate(test_data_3))
	nps_acc.append(backoff3_3[-1].evaluate(test_data_3))
	nps_acc.append(backoff4_3[-1].evaluate(test_data_3))
	nps_acc.append(backoff5_3[-1].evaluate(test_data_3))

	x = [1,2,3,4,5]
	plt.plot(x,conll_acc,'-ok',color = 'b',label="WSJ")
	plt.plot(x,brown_acc,'-ok',color = 'g',label="Brown")
	plt.plot(x,nps_acc,'-ok',color = 'r',label="NPS Chat")
	plt.xlabel("N")
	plt.ylabel("Accuracy")
	x_ticks = np.arange(1,6,1)
	plt.xticks(x_ticks)
	plt.legend()
	#plt.show()
	plt.savefig('backoff_acc.pdf')



	"""
	print(backoff1[-1].evaluate(test_data))
	print(backoff2[-1].evaluate(test_data))
	print(backoff3[-1].evaluate(test_data))
	print(backoff4[-1].evaluate(test_data))
	print(backoff5[-1].evaluate(test_data))
	print(perceptron.evaluate(test_data))
	print(perceptron.evaluate(test_data))
	"""




