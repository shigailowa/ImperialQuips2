import nltk
import gensim.downloader as api 
from nltk.corpus import wordnet as wn 


#Word Similarity
#suggest words to replace given word with
def suggest_replacement(word):

	#GloVe Vectors, cosine similarity
	#word_vectors = api.load("glove-wiki-gigaword-50")
	#sim_words = word_vectors.most_similar(word,topn=3)

	#WordNet
	sim_words_wn = []

	for syn in wn.synsets(word):
		print(syn)
		print(syn.name())
		print(syn.pos())
		print(syn.similar_tos())
		#sim_words_wn.append(syn)
		#for l in syn.lemmas():
		#	print(l)
		#	print(l.name())
			

	#return sim_words_wn

if __name__ == '__main__':

	word = 'small'
	suggest_replacement(word)