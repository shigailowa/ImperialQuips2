import nltk
from nltk.chunk.regexp import ChunkString, ChunkRule, ChinkRule
from nltk.tree import Tree
from nltk.chunk import RegexpParser
from nltk.corpus import conll2000

#Rule-based chunking
def regexp_chunk(sentence):
	#define rules here
	grammar = r"""CHUNK: 
					  {<DT|PP|PRP\$>?<JJ>*<NN>}
					  {<V.*><TO><V.*>}
			   """
	cp = nltk.RegexpParser(grammar)
	chunks = cp.parse(tags)

	#ngram chunker
	return chunks

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


#Unigram chunking
def unigram_chunk():
	test_sents = conll2000.chunked_sents('test.txt')
	train_sents = conll2000.chunked_sents('train.txt')
	unigram_chunker = UnigramChunker(train_sents)
	print(unigram_chunker.evaluate(test_sents))
	text = nltk.word_tokenize('My yellow dog loves eating breakfast and I like to watch netflix')
	tags = nltk.pos_tag(text)
	print(unigram_chunker.parse(tags))

def bigram_chunk():
	test_sents = conll2000.chunked_sents('test.txt')
	train_sents = conll2000.chunked_sents('train.txt')
	bigram_chunker = BigramChunker(train_sents)
	print(bigram_chunker.evaluate(test_sents))
	text = nltk.word_tokenize('My yellow dog loves eating breakfast and I like to watch netflix')
	tags = nltk.pos_tag(text)
	print(bigram_chunker.parse(tags))

#Phrase Segmentation
#Chunking
def split_phrases():

	#unigram_chunk()
	bigram_chunk()
	#get POS tags of sentence first
	#text = nltk.word_tokenize(sentence)
	#tags = nltk.pos_tag(text)


if __name__ == '__main__':

	#msg = "i like to read, play video games and watch netflix. what about you? do you have any hobbies?"
	#phrase = "i like to read, play video games and watch netflix"

	split_phrases()