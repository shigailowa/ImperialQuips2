import nltk
from nltk.tag import NgramTagger
from nltk.corpus import conll2000


#general N-gram tagger
#works for every N
def ngram_tagger(n,backoff=None):
	train_data = conll2000.tagged_sents('train.txt')
	Ngram_Tagger = NgramTagger(n,train_data,backoff=backoff)
	return(Ngram_Tagger)

#Backoff Tagging
def backoff_tagger():

	t0 = nltk.DefaultTagger('NN')
	t1 = ngram_tagger(1,backoff=t0)
	t2 = ngram_tagger(2,backoff=t1)
	t3 = ngram_tagger(3,backoff=t2)

	test_data = conll2000.tagged_sents('test.txt')
	print(t3.evaluate(test_data))



##Greedy Average Perceptron tagger
#used and recommended by nltk
def perceptron_tagger(phrase):
	text = nltk.word_tokenize(phrase)
	tags = nltk.pos_tag(text)
	return(tags)


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
	
	backoff_tagger()

