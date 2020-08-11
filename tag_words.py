# -*- encoding: cp852 -*-

import nltk
from nltk.tag import NgramTagger
from nltk.tag import PerceptronTagger
from nltk.corpus import conll2000
from nltk.corpus import webtext
from nltk.corpus import brown
from nltk.corpus import nps_chat
from nltk.corpus import cess_esp
from nltk.corpus import indian
from nltk.corpus import ConllCorpusReader
from nltk.corpus import BracketParseCorpusReader
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


def read_german():
	corp = ConllCorpusReader('.','tiger_release_aug07.corrected.16012013.conll09',
							['ignore','words','ignore','ignore','pos'],encoding='utf-8')


	return(corp)


def read_russian(data):
	corp = ConllCorpusReader('.', data, 
							['ignore','words','ignore','pos','ignore','ignore','ignore','ignore','ignore','ignore'], encoding='utf-8')
	return(corp)


if __name__ == '__main__':

	#print(tag_words("play football and watch netflix"))

	train_data_rus = read_russian('russ_train_new.conll').tagged_sents()
	test_data_rus = read_russian('russ_test_new.conll').tagged_sents()
	#size = int(len(germo.tagged_sents())*0.8)
	#train_data_ge = germo.tagged_sents()[:size]
	#test_data_ge = germo.tagged_sents()[size:]

	#different Datasets
	
	""""
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

	#spanish
	"""
	size = int(len(cess_esp.tagged_sents())*0.8)
	train_data_sp = cess_esp.tagged_sents()[:size]
	test_data_sp = cess_esp.tagged_sents()[size:]
	"""

	"""
	#indian
	size = int(len(indian.tagged_sents())*0.8)
	train_data_in = indian.tagged_sents()[:size]
	test_data_in = indian.tagged_sents()[size:]
	train_data_in_2 = [x for i,x in enumerate(train_data_in) if (i!=134 and i!=2104 and i!=2105 and i!=2108)]
	"""
	
	"""
	for i, sen in enumerate(train_data_in):
		for j, (word, pos) in enumerate(sen):
			if not word:
				print(i)
				print(j)
	"""
		
	#train different Taggers
	#simple Ngram
	
	"""
	unigram_1 = ngram_tagger(1,train_data = train_data_rus)
	bigram_1 = ngram_tagger(2,train_data = train_data_rus)
	trigram_1 = ngram_tagger(3,train_data = train_data_rus)
	fourgram_1 = ngram_tagger(4,train_data = train_data_rus)
	fivegram_1 = ngram_tagger(5,train_data = train_data_rus)
	"""

	"""

	unigram_2 = ngram_tagger(1,train_data = train_data_por)
	bigram_2 = ngram_tagger(2,train_data = train_data_por)
	trigram_2 = ngram_tagger(3,train_data = train_data_por)
	fourgram_2 = ngram_tagger(4,train_data = train_data_por)
	fivegram_2 = ngram_tagger(5,train_data = train_data_por)

	unigram_3 = ngram_tagger(1,train_data = train_data_in)
	bigram_3 = ngram_tagger(2,train_data = train_data_in)
	trigram_3 = ngram_tagger(3,train_data = train_data_in)
	fourgram_3 = ngram_tagger(4,train_data = train_data_in)
	fivegram_3 = ngram_tagger(5,train_data = train_data_in)
	"""

	"""
	backoff1_1 = backoff_tagger(1,train_data = train_data_rus)
	backoff2_1 = backoff_tagger(2,train_data = train_data_rus)
	backoff3_1 = backoff_tagger(3,train_data = train_data_rus)
	backoff4_1 = backoff_tagger(4,train_data = train_data_rus)
	backoff5_1 = backoff_tagger(5,train_data = train_data_rus)
	"""

	"""

	backoff1_2 = backoff_tagger(1,train_data = train_data_in)
	backoff2_2 = backoff_tagger(2,train_data = train_data_in)
	backoff3_2 = backoff_tagger(3,train_data = train_data_in)
	backoff4_2 = backoff_tagger(4,train_data = train_data_in)
	backoff5_2 = backoff_tagger(5,train_data = train_data_in)
	"""

	"""
	backoff1_3 = backoff_tagger(1,train_data = train_data_3)
	backoff2_3 = backoff_tagger(2,train_data = train_data_3)
	backoff3_3 = backoff_tagger(3,train_data = train_data_3)
	backoff4_3 = backoff_tagger(4,train_data = train_data_3)
	backoff5_3 = backoff_tagger(5,train_data = train_data_3)
	"""

	"""
	#Backoff Taggers
	backoff1 = backoff_tagger(1,train_data_new)
	backoff2 = backoff_tagger(2,train_data_new)
	backoff3 = backoff_tagger(3,train_data_new)
	backoff4 = backoff_tagger(4,train_data_new)
	backoff5 = backoff_tagger(5,train_data_new)
	"""
	
	#Perceptron Tagger
	perceptron = perceptron_tagger(train_data_rus)
	print(perceptron.evaluate(test_data_rus))

	
	#Evaluate Taggers
	"""
	conll_acc = []
	conll_acc.append(backoff1_1[-1].evaluate(test_data_rus))
	conll_acc.append(backoff2_1[-1].evaluate(test_data_rus))
	conll_acc.append(backoff3_1[-1].evaluate(test_data_rus))
	conll_acc.append(backoff4_1[-1].evaluate(test_data_rus))
	conll_acc.append(backoff5_1[-1].evaluate(test_data_rus))

	brown_acc = []
	brown_acc.append(unigram_1.evaluate(test_data_rus))
	brown_acc.append(bigram_1.evaluate(test_data_rus))
	brown_acc.append(trigram_1.evaluate(test_data_rus))
	brown_acc.append(fourgram_1.evaluate(test_data_rus))
	brown_acc.append(fivegram_1.evaluate(test_data_rus))
	"""

	"""	
	nps_acc = []
	nps_acc.append(unigram_3.evaluate(test_data_in))
	nps_acc.append(bigram_3.evaluate(test_data_in))
	nps_acc.append(trigram_3.evaluate(test_data_in))
	nps_acc.append(fourgram_3.evaluate(test_data_in))
	nps_acc.append(fivegram_3.evaluate(test_data_in))
	"""

	#print(conll_acc)
	#print(brown_acc)
	#print(nps_acc)


	"""
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


	"""
	print(backoff1[-1].evaluate(test_data))
	print(backoff2[-1].evaluate(test_data))
	print(backoff3[-1].evaluate(test_data))
	print(backoff4[-1].evaluate(test_data))
	print(backoff5[-1].evaluate(test_data))
	print(perceptron.evaluate(test_data))
	print(perceptron.evaluate(test_data))
	"""




