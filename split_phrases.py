import nltk
from nltk.chunk.regexp import ChunkString, ChunkRule, ChinkRule
from nltk.tree import Tree
from nltk.chunk import RegexpParser
from nltk.corpus import conll2000


#class for Unigram Chunking
class UnigramChunker(nltk.ChunkParserI):

    def __init__(self, train_sents):
        train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)]
                      for sent in train_sents]
        self.tagger = nltk.UnigramTagger(train_data)

    def parse(self, sentence):
        pos_tags = [pos for (word,pos) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        conlltags = [(word, pos, chunktag) for ((word,pos),chunktag)
                     in zip(sentence, chunktags)]
        return nltk.chunk.conlltags2tree(conlltags)


#class for Bigram Chunking
class BigramChunker(nltk.ChunkParserI):

    def __init__(self, train_sents):
        train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)]
                      for sent in train_sents]
        self.tagger = nltk.BigramTagger(train_data)

    def parse(self, sentence):
        pos_tags = [pos for (word,pos) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        conlltags = [(word, pos, chunktag) for ((word,pos),chunktag)
                     in zip(sentence, chunktags)]
        return nltk.chunk.conlltags2tree(conlltags)


#Rule-based chunking
def regexp_chunk():
	#define rules here
	grammar = r"""NP: {<DT|PP|PRP\$>?<JJ>*<NN>}
				  VP: {<V.*>+<TO>?<V.*>*}
				  PP: {<IN>+|<TO>}
			   """
	cp = nltk.RegexpParser(grammar)
	return(cp)


#train Unigram chunker on conll2000 dataset
def unigram_chunk():
	train_sents = conll2000.chunked_sents('train.txt')
	unigram_chunker = UnigramChunker(train_sents)
	return(unigram_chunker)


#train Bigram chunker on conll2000 dataset
def bigram_chunk():
	train_sents = conll2000.chunked_sents('train.txt')
	bigram_chunker = BigramChunker(train_sents)
	return(bigram_chunker)


#Compare different chunkers
def split_phrases(regexp_chunker, unigram_chunker, bigram_chunker):

	test_sents = conll2000.chunked_sents('test.txt')
	print(regexp_chunker.evaluate(test_sents))
	print(unigram_chunker.evaluate(test_sents))
	print(bigram_chunker.evaluate(test_sents))

	"""
	text = nltk.word_tokenize('My yellow dog loves eating breakfast and I like to watch netflix')
	tags = nltk.pos_tag(text)
	print(unigram_chunker.parse(tags))
	"""


if __name__ == '__main__':

	
	regexp_chunker = regexp_chunk()
	unigram_chunker = unigram_chunk()
	bigram_chunker = bigram_chunk()

	"""
	phrase = "My yellow dog has been asking to eat the whole day because of hunger"
	text = nltk.word_tokenize(phrase)
	tags = nltk.pos_tag(text)

	print(regexp_chunker.parse(tags))
	print(unigram_chunker.parse(tags))
	print(bigram_chunker.parse(tags))
	"""

	split_phrases(regexp_chunker,unigram_chunker,bigram_chunker)
	