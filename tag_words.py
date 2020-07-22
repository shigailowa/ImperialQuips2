import nltk
from nltk.tag import NgramTagger
from nltk.corpus import conll2000


#general N-gram tagger
#works for every N
def ngram_tagger(n,phrase):
	train_data = conll2000.tagged_sents('train.txt')
	Ngram_Tagger = NgramTagger(n,train_data)
	test_data = conll2000.tagged_sents('test.txt')
	print(Ngram_Tagger.evaluate(test_data))
	print(Ngram_Tagger.tag(phrase))


##Greedy Average Perceptron tagger
#used and recommended by nltk
def perceptron_tagger(phrase):
	text = nltk.word_tokenize(phrase)
	tags = nltk.pos_tag(text)
	return tags


#Part-of-Speech Tagging
#split phrase into parts of speech 
def tag_words(phrase):

	#call different taggers here and compare


	return None



if __name__ == '__main__':

	phrase = "I like dogs"
	phrase = nltk.word_tokenize(phrase)
	ngram_tagger(1,phrase)

