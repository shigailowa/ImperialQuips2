import nltk
from nltk.tag import NgramTagger
from nltk.tag import PerceptronTagger
from nltk.corpus import conll2000


#general N-gram tagger
#works for every N
def ngram_tagger(n,backoff=None):
	train_data = conll2000.tagged_sents('train.txt')
	Ngram_Tagger = NgramTagger(n,train_data,backoff=backoff)
	return(Ngram_Tagger)

#Backoff Tagging
def backoff_tagger(n):

	t0 = nltk.DefaultTagger('NN')

	taggers = [t0]

	for i in range(n):
		taggers.append(ngram_tagger(i+1,backoff=taggers[i]))

	test_data = conll2000.tagged_sents('test.txt')

	print(taggers[n-1].evaluate(test_data))



##Greedy Average Perceptron tagger
#used and recommended by nltk
def perceptron_tagger():
	tagger = PerceptronTagger()
	test_data = conll2000.tagged_sents('test.txt')
	#text = nltk.word_tokenize(phrase)
	#tags = nltk.pos_tag(text)
	print(tagger.evaluate(test_data))


#Compare different taggers to each other
def tag_words():

	test_data = conll2000.tagged_sents('test.txt')
	unigram = ngram_tagger(1)
	bigram = ngram_tagger(2)
	trigram = ngram_tagger(3)
	fourgram = ngram_tagger(4)
	print(unigram.evaluate(test_data))
	print(bigram.evaluate(test_data))
	print(trigram.evaluate(test_data))
	print(fourgram.evaluate(test_data))




if __name__ == '__main__':

	"""
	phrase = "I like dogs because of their cuteness"
	print(perceptron_tagger(phrase))
	"""
	#tag_words()
	#backoff_tagger(1)
	#backoff_tagger(2)
	#backoff_tagger(3)
	#backoff_tagger(4)
	#backoff_tagger(5)
	perceptron_tagger()

